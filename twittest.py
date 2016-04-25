import cvxopt
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

import commdet as cd

# inputs a file of edge pairs, outputs adjacency matrix
def file_to_dense_matrix(f):
    id_dict = {}
    edges = []
    idx = 0
    for line in f:
        e = str.split(line)
        if e[0] not in id_dict:
            id_dict[e[0]] = idx
            idx += 1
        if e[1] not in id_dict:
            id_dict[e[1]] = idx
            idx += 1
        edges.append(e)
    N = idx+1
    A = cvxopt.matrix(0.,(N,N))
    for e in edges:
        A[id_dict[e[0]],id_dict[e[1]]] = 1.
    return A


# TEST CODE: Twitter 'ego' graph, files from https://snap.stanford.edu/data/egonets-Twitter.html
# FILE_ID = '400867704'
FILE_ID = '16834201'
EDGE_FILE = open('twitter/' + FILE_ID + '.edges', 'r')
A = file_to_dense_matrix(EDGE_FILE)
com = cd.A_to_com(A)
cd.plot_graph(A,com)
