from browser import window

import sys

class RegularOut:
    # Doesn't need self as an argument now??
    # It causes errors if its there... TODO: investigate further
    def write(text):
        window.write(str(text), 0)

class ErrorOut:
    # Doesn't need self as an argument now??
    # It causes errors if its there... TODO: investigate further
    def write(text):
        window.write(str(text), 1)

sys.stdout = RegularOut
sys.stderr = ErrorOut

# Finish setup

from graph import Graph

G = Graph(directed=False)

G.random(10, 20)

graph = G.export(0)

for i in graph:
    print(*i)

for i in range(100):
    print(i)
