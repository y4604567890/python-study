import networkx as nx
import matplotlib.pyplot as plt

NODE_AMOUNT = 20

g = nx.complete_graph(5)

g = nx.Graph()

g.add_nodes_from(range(NODE_AMOUNT))

# Draw a tree in graph
for i in range(NODE_AMOUNT):
    if i*2+1 < NODE_AMOUNT:
        g.add_edge(i, i*2+1)
    if i*2+2 < NODE_AMOUNT:
        g.add_edge(i, i*2+2)

plt.subplot(131)
nx.draw(g, with_labels=True)

plt.subplot(132)
nx.draw(g, with_labels=True, pos = nx.fruchterman_reingold_layout(g))

import numpy as np
plt.subplot(133)
nx.draw(g, with_labels=True, pos = nx.shell_layout(g))

plt.show()
