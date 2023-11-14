# Generates a grid of width * height

G = Graph(directed=True)

WIDTH = 10
HEIGHT = 10

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