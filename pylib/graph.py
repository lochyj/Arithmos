import random
import time
import uuid

from globals import *

from browser import window
import javascript # For null...

# A list of graphs that have been created.
# It is used to set the main graph (the being displayed)
# when the user calls Screen.display().
graphs = []

class Graph:

    def __init__(self, directed: bool = False):
        self.directed = directed
        window.setDirectional(directed)

        self.nodes: list[int] = []
        self.edges: list[int] = []

        self.nodes_attributes = {}
        self.edges_attributes = {}

        # This is an artifact of using a terribly written JS library.
        # It stores the index of the node / edge so that when we need
        # to modify it on the actual graph object that the library is using,
        # we dont have to search through all of the nodes / edges to
        # find the one we are referencing.
        self.node_index = {}
        self.edge_index = {}

        self.id = str(uuid.uuid4())

        if len(graphs) == 0:
            self.is_main = True
        else:
            self.is_main = False

        graphs.append(self)

    # ------------------|
    # Utility functions |
    # ------------------|

    # Sets the directedness of the graph
    def set_directed(self, directed: bool):
        self.directed = directed
        window.setDirectional(directed)
    
    def get_nodes(self):
        return self.nodes.copy()

    # Returns the edges in the graph in the specified format.
    # Defaults to connection list.
    def get_edges(self):
        return self.edges.copy()

    # This is kind of a bad design I will fix it in the future.
    def __set_main_graph(self):

        for graph in graphs:
            graph.__set_not_main_graph()

        self.is_main = True

    def __set_not_main_graph(self):
        self.is_main = False

    # ----------------
    # Nodes / Vertices
    # ----------------

    def add_node(self, node: any, label: str = "", colour: str = "#3183ba"):
        check_hashable_type(node)
        node = hash(node)
        self.nodes.append(node)

        if (label == ""):
            label = str(node)

        self.nodes_attributes[node] = {
            "label": label,
            "color": colour
        }

        window.addNode(self.id + str(node), label, colour)


    def remove_node(self, node: any):
        check_hashable_type(node)
        node = hash(node)

        if node not in self.nodes:
            return

        self.nodes.remove(node)

        window.removeNode(self.id + str(node))

        if node in self.nodes_attributes.keys():
            del self.nodes_attributes[node]

        for edge in self.edges:
            if edge[0] == node or edge[1] == node:
                if self.directed:
                    self.remove_edge(edge[0], edge[1])

                    window.removeEdge(self.id + str(edge[0]), self.id + str(edge[1]))
                else:
                    self.remove_edge(edge[0], edge[1])
                    self.remove_edge(edge[1], edge[0])

                    window.removeEdge(self.id + str(edge[0]), self.id + str(edge[1]))
                    window.removeEdge(self.id + str(edge[1]), self.id + str(edge[0]))

    def set_node_attribute(self, node: any, attribute: str, value: any):
        check_hashable_type(node)
        node = hash(node)

        if node not in self.nodes:
            print("WARN: Node not found.")
            return

        self.nodes_attributes[node] = {
            attribute: value
        }

        match attribute:
            case "label":
                # Label will always be a string.
                window.modifyNode(self.id + str(node), str(value), javascript.UNDEFINED)
            case "weight":
                ...
            case "color":
                ...
            case _:
                ...
    
    def get_node_attribute(self, node: any, attribute: str):
        check_hashable_type(node)
        node = hash(node)

        if node not in self.nodes:
            print("WARN: Node not found.")
            return

        return self.nodes_attributes[node][attribute]

    # -----
    # Edges
    # -----

    def add_edge(self, node_u: any, node_v: any, colour: str = "grey"):
        check_hashable_type(node_u)
        check_hashable_type(node_v)

        node_u = hash(node_u)
        node_v = hash(node_v)

        if self.directed:
            self.edges.append((node_u, node_v))

            index = window.addEdge(self.id + str(node_u), self.id + str(node_v), colour)

            edge = hash((node_u, node_v))

            self.edge_index[edge] = index

        else:
            self.edges.append((node_u, node_v))
            self.edges.append((node_v, node_u))

            index_a = window.addEdge(self.id + str(node_u), self.id + str(node_v), "", colour)
            index_b = window.addEdge(self.id + str(node_v), self.id + str(node_u), "", colour)
    
    def remove_edge(self, node_u: any, node_v: any):
        check_hashable_type(node_u)
        check_hashable_type(node_v)

        node_v = hash(node_v)
        node_u = hash(node_u)

        if self.directed:
            self.edges.remove((node_u, node_v))

            window.removeEdge(self.id + str(node_u), self.id + str(node_v))

            edge = hash((node_u, node_v))

            if edge in self.edges_attributes.keys():
                del self.edges_attributes[edge]

        else:
            try:
                self.edges.remove((node_u, node_v))
                self.edges.remove((node_v, node_u))
            except ValueError:
                ... # Do nothing

            window.removeEdge(self.id + str(node_u), self.id + str(node_v))
            window.removeEdge(self.id + str(node_v), self.id + str(node_u))

            edge_a = hash((node_u, node_v))
            edge_b = hash((node_v, node_u))

            if edge_a in self.edges_attributes.keys():
                del self.edges_attributes[edge_a]

            
            if edge_b in self.edges_attributes.keys():
                del self.edges_attributes[edge_b]



    def set_edge_attribute(self, node_u: any, node_v: any, attribute: str, value: any):
        check_hashable_type(node_u)
        check_hashable_type(node_v)

        node_u = hash(node_u)
        node_v = hash(node_v)

        if self.directed:
            edge = hash((node_u, node_v))

            if (node_u, node_v) not in self.edges:
                print("WARN: Edge not found.")
                return

            self.nodes_attributes[edge] = {
                attribute: value
            }

        else:
            edge_a = hash((node_u, node_v))
            edge_b = hash((node_v, node_u))

            if (node_u, node_v) not in self.edges or (node_v, node_u) not in self.edges:
                print("WARN: Edge not found.")
                return

            self.nodes_attributes[edge_a] = {
                attribute: value
            }

            self.nodes_attributes[edge_b] = {
                attribute: value
            }
        
    
    def get_edge_attribute(self, node_u: any, node_v: any, attribute: str):
        check_hashable_type(node_u)
        check_hashable_type(node_v)

        node_u = hash(node_u)
        node_v = hash(node_v)
        
        if self.directed:
            edge = hash((node_u, node_v))

            if (node_u, node_v) not in self.edges:
                print("WARN: Edge not found.")
                return

            return self.nodes_attributes[edge][attribute]

        else:
            edge_a = hash((node_u, node_v))
            edge_b = hash((node_v, node_u))

            if (node_u, node_v) not in self.edges or (node_v, node_u) not in self.edges:
                print("WARN: Edge not found.")
                return

            value_a = self.nodes_attributes[edge_a][attribute]
            value_b = self.nodes_attributes[edge_b][attribute]

            if value_a != value_b:
                print("WARN: Edge values do not match.\nWe returned the first value we found.")
                return value_a
            
            return value_a

    # ----------------
    # Other observers
    # ----------------

    def adjacent(self, node_u: any, node_v: any):
        check_hashable_type(node_u)
        check_hashable_type(node_v)

        node_u = hash(node_u)
        node_v = hash(node_v)

        if self.directed:
            if (node_u, node_v) in self.edges:
                return True
            else:
                return False
        else:
            if (node_u, node_v) in self.edges or (node_v, node_u) in self.edges:
                return True
            else:
                return False

    def neighbours(self, node: any):
        # TODO: Make this a little more readable...

        check_hashable_type(node)

        node = hash(node)

        if self.directed:
            edges = []

            for edge in self.edges:
                if edge[0] == node:
                    edges.append(edge[1])

            return edges

        else:
            edges = []

            for edge in self.edges:
                if edge[0] == node:
                    edges.append(edge[1])
                elif edge[1] == node:
                    edges.append(edge[0])

            return edges


    # ----------------
    # Helper functions
    # ----------------

    # TODO: Make random never generate islands and only generate a single main graph.
    def random(self, num_nodes: int, num_edges: int):
        
        if len(self.nodes) > 0:

            print("WARN: Cannot generate a random graph with a non-empty graph!")
            print("Clearing the graph")

            nodes = self.nodes

            for node in nodes:
                self.remove_node(node)

            return

        if num_edges < num_nodes - 1:
            print("WARN: Cant make a random graph with that little edges.")
            print("Setting to minimum required edges")
            num_edges = num_nodes - 1

        for i in range(num_nodes):
            self.add_node(i)

        node_list = self.get_nodes()

        connected_list = []

        begin_node = random.choice(node_list)

        node_list.remove(begin_node)
        connected_list.append(begin_node)

        while len(node_list) > 0:
            node = random.choice(node_list)
            connection = random.choice(connected_list)

            self.add_edge(node, connection)

            node_list.remove(node)
            connected_list.append(node)

        iters = 0

        if self.directed:

            while len(self.edges) < num_edges:
                iters += 1

                if iters > num_edges * 2:
                    break

                node_u = random.choice(connected_list)
                node_v = random.choice(connected_list)

                if node_u == node_v:
                    continue

                if self.adjacent(node_u, node_v):
                    continue

                self.add_edge(node_u, node_v)

        else:
            while (len(self.edges) / 2) < num_edges:
                iters += 1

                if iters > num_edges * 2:
                    break

                node_u = random.choice(connected_list)
                node_v = random.choice(connected_list)

                if node_u == node_v:
                    continue

                if self.adjacent(node_u, node_v):
                    continue

                self.add_edge(node_u, node_v)

    # Returns a adjacency matrix of the graph.
    def export(self):

        matrix = []

        for i in range(len(self.nodes)):
            matrix.append([])
            for j in range(len(self.nodes)):
                matrix[i].append(0)

        for edge in self.edges:
            matrix[edge[0]][edge[1]] = 1

        return matrix


    # -----------|
    # Animations |
    # -----------|

    def traverse(self, node_u: any, node_v: any, colour: str = "green", delay: float = 1):
        check_hashable_type(node_u)
        check_hashable_type(node_v)

        node_u = hash(node_u)
        node_v = hash(node_v)

        delay = delay * 1000

        if self.directed:
            if (node_u, node_v) not in self.edges:
                print("WARN: Edge not found.")
                return

            self.set_edge_attribute(node_u, node_v, "visited", True)

            window.traverse_edge(self.id + str(node_u), self.id + str(node_v), colour, self.directed, delay)

        else:
            if (node_u, node_v) not in self.edges or (node_v, node_u) not in self.edges:
                print("WARN: Edge not found.")
                return

            self.set_edge_attribute(node_u, node_v, "visited", True)
            self.set_edge_attribute(node_v, node_u, "visited", True)

            window.traverse_edge(self.id + str(node_u), self.id + str(node_v), colour, self.directed, delay)

    def visit(self, node: any, colour: str = "green", delay: float = 1):
        check_hashable_type(node)

        node = hash(node)

        if node not in self.nodes:
            print("WARN: Node not found.")
            return

        delay = delay * 1000

        window.visit_node(self.id + str(node), colour, delay)