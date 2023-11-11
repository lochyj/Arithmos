import random

from libs.globals import *

# What is int|float|str|tuple?
# We type hint int|float|str|tuple as the type for
# all of the edge and node values as they are 
# hashable types. This means we can convert them to 
# an int through the hash() functions.

class Graph:
    
    def __init__(self, directed: bool = False):
        self.directed = directed

        self.nodes: list[int] = []
        self.edges: list[int] = []

        self.nodes_attributes = {}
        self.edges_attributes = {}

    # ------------------|
    # Utility functions |
    # ------------------|

    def __str__(self):
        # Define what happens when the user prints the class object.
        print("Not implemented yet :)")

    # Sets the directedness of the graph
    def set_directed(self, directed: bool):
        self.directed = directed
    
    def get_nodes(self):
        return self.nodes
    
    # Returns the edges in the graph in the specified format.
    # Defaults to connection list.
    def get_edges(self, format: int = CONNECTION_LIST):
        match format:
            case 0:
                return self.edges
            
            case 1:
                return None
            
            case _: # Default pattern
                return None


    # ----------------
    # Nodes / Vertices
    # ----------------

    def add_node(self, node: node_id):
        node = hash(node)
        self.nodes.append(node)
        

    def remove_node(self, node: node_id):
        node = hash(node)
        self.nodes.remove(node)

        if node in self.nodes_attributes.keys():
            del self.nodes_attributes[node]
        
        for edge in self.edges:
            if edge[0] == node or edge[1] == node:
                if self.directed:
                    self.remove_edge(edge[0], edge[1])
                else:
                    self.remove_edge(edge[0], edge[1])
                    self.remove_edge(edge[1], edge[0])

    
    def set_node_attribute(self, node: node_id, attribute: str, value: any):
        node = hash(node)

        if node not in self.nodes:
            print("WARN: Node not found.")
            return

        self.nodes_attributes[node] = {
            attribute: value
        }
    
    def get_node_attribute(self, node: node_id, attribute: str):
        node = hash(node)

        if node not in self.nodes:
            print("WARN: Node not found.")
            return

        return self.nodes_attributes[node][attribute]

    # -----
    # Edges
    # -----

    def add_edge(self, node_u: node_id, node_v: node_id):
        node_u = hash(node_u)
        node_v = hash(node_v)

        if self.directed:
            self.edges.append((node_u, node_v))
        else:
            self.edges.append((node_u, node_v))
            self.edges.append((node_v, node_u))
    
    def remove_edge(self, node_u: node_id, node_v: node_id):
        node_v = hash(node_v)
        node_u = hash(node_u)

        if self.directed:
            self.edges.remove((node_u, node_v))
            
            edge = hash((node_u, node_v))

            if edge in self.edges_attributes.keys():
                del self.edges_attributes[edge]

        else:
            try:
                self.edges.remove((node_u, node_v))
                self.edges.remove((node_v, node_u))
            except ValueError:
                ... # Do nothing

            edge_a = hash((node_u, node_v))
            edge_b = hash((node_v, node_u))

            if edge_a in self.edges_attributes.keys():
                del self.edges_attributes[edge_a]
            
            if edge_b in self.edges_attributes.keys():
                del self.edges_attributes[edge_b]


    def set_edge_attribute(self, node_u: node_id, node_v: node_id, attribute: str, value: any):
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
        
    
    def get_edge_attribute(self, node_u: node_id, node_v: node_id, attribute: str):
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

    def adjacent(self, node_u: node_id, node_v: node_id):
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

    def neighbours(self, node: node_id):
        # TODO: Make this a little more readable...
        
        node = hash(node)

        if self.directed:
            return [edge[1] for edge in self.edges if edge[0] == node]
        
        else:
            return [edge[1] for edge in self.edges if edge[0] == node or edge[1] == node]


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

        node_list = [i for i in range(num_nodes)]

        for i in range(num_edges):
            connection = random.choices(node_list, k=2)

            iters = 0

            while connection[0] == connection[1] and iters < 10:
                connection = random.choices(node_list, k=2)
                iters += 1

            self.add_edge(connection[0], connection[1])
    
    def export(self, type):

        match type:
            case 0:
                matrix = []

                for i in range(len(self.nodes)):
                    matrix.append([])
                    for j in range(len(self.nodes)):
                        matrix[i].append(0)

                for edge in self.edges:
                    matrix[edge[0]][edge[1]] = 1
                
                return matrix

            case _:
                return None

