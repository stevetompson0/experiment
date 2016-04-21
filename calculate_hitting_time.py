__author__ = 'steve'

import networkx as np
import numpy as np
from numpy import linalg


# get transition matrix
def get_transition_matrix(G):
    n = G.number_of_nodes()
    print "total number of nodes : " + str(n)
    node_list = G.nodes()
    res = np.zeros((n, n), dtype='float64')
    for i in node_list:
        # i-th row in transition matrix
        deg = np.float_(G.degree(i))
        for j in range(n):
            # j-th col in transition matrix
            res[i, j] = np.divide(np.float_(G.number_of_edges(i, j)), deg)

    return res


def get_hitting_time_matrix(transition_matrix, output_file, index):
    """

    :param transition_matrix: transition matrix for this graph
    :return: hitting time matrix
             (i, j) is the H(j*, i), j* might not be node j
    """
    size = transition_matrix.shape[0] - 1
    I = np.identity(size)
    if (index + 1) * 1000 > size:
        upper_bound = size + 1
    else:
        upper_bound = (index + 1) * 1000
    node_range = range(index * 1000, upper_bound)

    for j in node_range:
        print "calculating " + str(j) + " out of " + str(size) + " row for hitting matrix"
        # delete j-th row
        print "delete j-th row"
        temp = np.delete(transition_matrix, j, 0)
        # delete j-th column
        print "delete j-th column"
        j_matrix = np.delete(temp, j, 1)

        print "construct ones"
        e = np.ones(size)
        print "calculating j_hitting time"
        j_hitting_time = (np.mat(linalg.inv(np.subtract(I, j_matrix))) * np.mat(e).transpose()).transpose()

        '''
        if j == 0:
            res = j_hitting_time
        else:
            res = np.concatenate((res, j_hitting_time), axis=0)
        '''

        print "calculating rwcc score for node " + str(j)

        output_file.write(str(j) + ' ' + str(np.divide(np.float_(1), j_hitting_time.sum())) + '\n')
        output_file.flush()
    #return res


def get_random_walk_closeness_centrality(hitting_time_matrix, row):
    res = np.float_(0)
    size = hitting_time_matrix.shape[1]
    for j in range(size):
        res += hitting_time_matrix[row, j]
    return np.divide(np.float_(1), res)


def get_random_walk_local_closeness_centrality(hitting_time_matrix, row):
    res = np.float_(0)
    size = hitting_time_matrix.shape[1]
    for j in range(size):
        res += np.divide(np.float_(1), hitting_time_matrix[row, j])
    return np.divide(res, size)
