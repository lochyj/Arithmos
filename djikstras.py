from libs.graph import Graph
from libs.set import Set

from libs.globals import *

from sys import maxsize as infinity

G = Graph()

G.random(20, 35)

def dijkstras(source: node_id, destination: node_id):

    Q = Set()

    for vertex in G.get_nodes():
        G.set_node_attribute(vertex, "dist", infinity)
        Q.add(vertex)

    G.set_node_attribute(source, "dist", 0)

    while not Q.is_empty():
        u = ...