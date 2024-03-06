import numpy as np
from sklearn.manifold import SpectralEmbedding

def eigenmap(x, y, z, n_neighbors=10):
    xyz = np.array([x, y, z]).T
    embedding = SpectralEmbedding(n_neighbors=n_neighbors)
    return embedding.fit_transform(xyz)