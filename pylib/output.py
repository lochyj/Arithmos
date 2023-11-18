from browser import window

# A simple interface class for the visualization panel of Arithmos.

class Output:
    def __init__(self):
        self.graph = window.getGraph()

    def focus(self):
        self.graph.zoomToFit(0, 0)