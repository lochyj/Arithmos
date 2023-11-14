
# ----------------|
# Brython imports |
# ----------------|

from browser import window, document

import sys

# --------------|
# Arithmos core |
# --------------|

from graph import Graph
from set import Set
from priority_queue import PriorityQueue
# from queue import Queue
# from array import Array
# from list import List
#from stack import Stack

# ------------|
# Setup stdio |
# ------------|

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

# --------------|
# Setup buttons |
# --------------|

def button_run(_):
    window.saveCode()
    text = window.getCode()

    exec(text)

def button_stop(_):
    ...

def button_reset(_):
    button_stop(0)
    button_run(0)

document["run"].bind("click", button_run)
document["stop"].bind("click", button_stop)
document["reset"].bind("click", button_reset)

print("Loading finished!")