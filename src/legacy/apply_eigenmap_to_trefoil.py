import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import SpectralEmbedding

from src.legacy.trefoil_sampler import TrefoilSampler

def plot(x, y):
    fig = plt.figure(figsize=(9, 9), facecolor="w")
    ax = fig.add_subplot(111)
    ax.scatter(x, y)
    plt.savefig('png/apply_eigenmap_to_trefoil.png')

def main():
    N = 1000
    sampler = TrefoilSampler(N)
    x, y, z = sampler.sample()
    
    # 1次元の図形なので近傍点の個数はデフォルトより少なめに設定すること
    emmbeding = SpectralEmbedding(n_neighbors=10)
    
    X = np.array([x, y, z]).T
    Y = emmbeding.fit_transform(X)
    plot(Y[:, 0], Y[:, 1])

if __name__ == "__main__":
    main()