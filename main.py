from libs.graph import Graph

G = Graph(directed=True)

G.add_node(0)
G.add_node(1)
G.add_node(2)

G.add_edge(0, 1)
G.add_edge(2, 1)

print(G.get_edges())
print(G.get_nodes())

G.set_node_attribute(0, "name", "John")
G.set_node_attribute(0, "name", "Doe")

print(G.get_node_attribute(0, "name"))

G.remove_node(2)

print(G.get_edges())
