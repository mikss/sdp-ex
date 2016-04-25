"""
COMMUNITY DETECTION VIA SDP
This file contains some quick code to:
    (1) read a list of edges;
    (2) solve a semidefinite program (SDP);
    (3) output the graph embedded in 2D, colored by community.
Some references:
    https://arxiv.org/pdf/1412.6156v2
    http://arxiv.org/pdf/1411.4686v4.pdf
    http://arxiv.org/pdf/1504.05910v3.pdf
    http://arxiv.org/pdf/1504.03987v2.pdf
"""

# TODO:
# belief propagation: http://arxiv.org/pdf/cond-mat/0604429.pdf
# non-backtracking: https://arxiv.org/pdf/1306.5550v2
# spectral methods: http://arxiv.org/pdf/1307.7729v1.pdf
# other empirically justified methods: https://cs.stanford.edu/people/jure/pubs/communities-www10.pdf

import cvxopt
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# inputs an adjacency matrix, outputs B matrix
#   B = 2A - (11^T - I): 0 if i=j, 1 if edge, -1 otherwise
def A_to_B(A):
    M,N = A.size
    B = 2 * A - cvxopt.matrix(1.0,(M,N)) + cvxopt.spmatrix(1.0, range(M), range(N))
    return B

# inputs a adjacency matrix, outputs a community vector
def A_to_com(A):
    B = A_to_B(A)
    N = B.size[0]
    cons_c = cvxopt.matrix([-1.] * N)
    G_rows = [N*i + i for i in range(N)]
    cons_G = [cvxopt.spmatrix([1.]*N, G_rows, list(range(N)))]
    cons_h = [-B]

    sol = cvxopt.solvers.sdp(c=cons_c, Gs=cons_G, hs=cons_h)
    opt = sol['zs'][0]

    w,v = np.linalg.eig(opt)
    com = np.sign(v[:,0])

    return com

def plot_graph(adj,com):
    color_dict = {-1.:'blue', 1.:'red'}
    colors = [ color_dict[c] for c in com ]
    G = nx.from_numpy_matrix(np.array(adj))
    nx.draw_networkx(G, arrows=True, with_labels=False, node_color=colors, node_size=100)
    plt.show()
