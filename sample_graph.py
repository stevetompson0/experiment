__author__ = 'steve'

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from calculate_hitting_time import *

G = nx.Graph()

node_list = []
for i in range(110):
    node_list.append(i)
# node_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
G.add_nodes_from(node_list)

# edge_list = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 13), (0, 14), (0, 15), (0, 16), (0, 17), (6, 7), (7, 8), (8, 9), (9, 10), (9, 11), (9, 12)]
edge_list = []
for i in range(1, 101):
    edge_list.append((0, i))
edge_list.append((100, 101))
edge_list.append((101, 102))
edge_list.append((102, 103))
edge_list.append((103, 104))

for i in range(105, 110):
    edge_list.append((104, i))
G.add_edges_from(edge_list)

# get transition matrix
transition_matrix = get_transition_matrix(G)

np.set_printoptions(precision=3)
hitting_time_matrix = get_hitting_time_matrix(transition_matrix)

# create labels
labels = {}
for node in node_list:
    # labels[node] = get_random_walk_closeness_centrality(hitting_time_matrix, node)
    labels[node] = get_random_walk_local_closeness_centrality(hitting_time_matrix, node)

# normalize
max_centrality = max(labels.values())
max_centrality = 1

for node in node_list:
    labels[node] = str(node) + ':' + "%.3f" % np.divide(labels[node], max_centrality)

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, labels)
print labels
plt.show()



