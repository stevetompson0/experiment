__author__ = 'steve'

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from calculate_hitting_time import *
import time

G = nx.Graph()
print "experiments start"
time0 = time.time()


print "start reading data"
for i in range(4039):
    G.add_node(i)

with open('facebook_combined.txt', 'r') as f:
    for line in f:
        edge = line.split()
        G.add_edge(int(edge[0]), int(edge[1]))

print "start getting transition matrix"
# get transition matrix
transition_matrix = get_transition_matrix(G)

np.set_printoptions(precision=3)

print "start getting hitting time matrix"
hitting_time_matrix = get_hitting_time_matrix(transition_matrix)

with open('facebook_combined_rwcc_score.txt', 'w+') as output_file:
    for node in range(4039):
        print "calculating rwcc score for node " + str(node)
        output_file.write(str(node) + ' ' + str(get_random_walk_closeness_centrality(hitting_time_matrix, node)))

print "finished"
print "time needed: " + str(time.time() - time0)

'''
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

'''

