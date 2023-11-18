from graph import Graph

from browser import window

class Screen():
    def display(graph_new: Graph):
        window.resetGraph()
        window.cancel_animation()
        window.resume()

        graph_new.__set_main_graph()

        for node in graph_new.nodes:
            window.addNode(node)

        for edge in graph_new.edges:
            window.addEdge(edge[0], edge[1])