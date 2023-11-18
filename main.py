
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
        window.write(str(text) + '\n', 1)

sys.stdout = RegularOut
sys.stderr = ErrorOut

# --------------|
# Setup buttons |
# --------------|

__running = False

__paused = False

def pause():
    global __paused
    __paused = not __paused

    # window.pause() is for the graph visualization library
    # and window.pause_animation() is for the animation script
    # TODO combine them...

    if __paused:
        window.pause()
        window.pause_animation()
        document["run"].html = """<img src="./icons/play.svg" alt="Run/Pause">Resume"""

    else:
        window.resume()
        window.resume_animation()
        document["run"].html = """<img src="./icons/pause.svg" alt="Run/Pause">Pause"""

def button_run(_):
    global __running
    if __running:
        # The user wants to pause now...
        pause()
        return
    window.saveCode()
    text = window.getCode()

    document["run"].html = """<img src="./icons/pause.svg" alt="Run/Pause">Pause"""

    __running = True

    exec(text)

def button_stop(_):
    global __running

    if not __running:
        return

    document["run"].html = """<img src="./icons/play.svg" alt="Run/Pause">Run"""

    window.resume()
    window.resetGraph()
    window.cancel_animation()
    __running = False

def button_restart(_):
    button_stop(0)
    button_run(0)

document["run"].bind("click", button_run)
document["stop"].bind("click", button_stop)
document["restart"].bind("click", button_restart)

print("Loading finished!")