from libs.graph import Graph

G = Graph(directed=False)

# G.add_node(0)
# G.add_node(1)
# G.add_node(2)

# G.add_edge(0, 1)
# G.add_edge(2, 1)

# G.set_node_attribute(0, "name", "John")
# G.set_node_attribute(0, "name", "Doe")

# print(G.get_edges())

# print(G.adjacent(2, 1))

G.random(10, 20)

graph = G.export(0)

for i in graph:
    print(*i)
