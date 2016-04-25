# Examples of Sparse PCA

# TODO: explore sparse PCA links to community detection: http://arxiv.org/abs/1406.5647

# Simulate data X with means MU and spiked covariance SIG
import numpy as np
N = 500
P = 10
MU = [0] * P
T = 1  # spike level
K = 2  # sparsity level
V = list(range(1,K+1)) + [0]*(P-K)
V = V / np.linalg.norm(V)
SIG = np.identity(P) + T * np.matrix(V).transpose() * np.matrix(V)
X = np.matrix(np.random.multivariate_normal(MU,SIG,N))

#####

# using scikit-learn method for Sparse PCA (like an l1-regularized dictionary learning problem)
from sklearn.decomposition import SparsePCA
spca = SparsePCA(n_components=1, alpha=5)
spca.fit(X)

from sklearn.decomposition import PCA
pca = PCA(n_components=1)
pca.fit(X)

print('Classical 1st principal component:', pca.components_)
print('Sparse 1st principal component:', spca.components_)

#####

# TODO: SDP implementation a la El Ghaoui, Bach, D'Aspremont
import cvxopt
# TWO CONSTRAINTS
# trace = 1 (multiply with identity)
# l1 norm <= k (multiply with all 1s matrix)
# change inequality to equality by slack
