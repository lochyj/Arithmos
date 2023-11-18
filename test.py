# Generates a grid of width * height

G = Graph(directed=False)

WIDTH = 5
HEIGHT = 5

for i in range(WIDTH * HEIGHT):
    G.add_node(i)

for i in range(WIDTH * HEIGHT):
    if i % WIDTH != 0:
        G.add_edge(i, i - 1)

    if i % WIDTH != WIDTH - 1:
        G.add_edge(i, i + 1)

    if i >= WIDTH:
        G.add_edge(i, i - WIDTH)

    if i < WIDTH * (HEIGHT - 1):
        G.add_edge(i, i + WIDTH)

target_node = 0

end_node = WIDTH * HEIGHT - 1

def djikstras(begin, end):
    ...

# Screen.display resets the graph that is being
# visualised and displays the new one just created

# The first graph made by the user calls this function
# on iteslf to create the visualisation
Screen.display(djikstras(target_node, end_node))