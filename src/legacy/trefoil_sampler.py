import numpy as np
import matplotlib.pyplot as plt

N = 100
ELEV = 90
AZIM = 0

class TrefoilSampler:
    def __init__(self, N):
        self.N = N

    def sample(self):
        t = np.random.uniform(0, 2*np.pi, self.N)
        x = np.sin(t) + 2*np.sin(2*t)
        y = np.cos(t) - 2*np.cos(2*t)
        z = -np.sin(3*t)
        return x, y, z

    def plot(self, x, y, z):
        fig = plt.figure(figsize=(9, 9), facecolor="w")
        ax = fig.add_subplot(111, projection="3d")
        ax.scatter(x, y, z)
        ax.view_init(elev = ELEV, azim = AZIM)
        plt.savefig('png/trefoil_randomly.png')

def main():
    sampler = TrefoilSampler(N)
    x, y, z = sampler.sample()
    sampler.plot(x, y, z)

if __name__ == "__main__":
    main()
