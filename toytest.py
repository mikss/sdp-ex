# TEST CODE: Stochastic block model with two communities

import cvxopt
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

import math
import commdet as cd

N = 50
M1 = N // 2
M2 = N - M1
truth = [1]*M1 + [-1]*M2

a = 3
b = 0.5
p = a * math.log(N) / N
q = b * math.log(N) / N

adj = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            pass
        elif truth[i] == truth[j]:
            adj[i][j] = np.random.binomial(1,p)
        else:
            adj[i][j] = np.random.binomial(1,q)

A = cvxopt.matrix(adj)
com = cd.A_to_com(A)
cd.plot_graph(A,com)
