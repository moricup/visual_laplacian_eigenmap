import numpy as np

from src.knot.core import Sampler

class TrefoilSampler(Sampler):
    def __init__(self, N):
        self.N = N

    def sample(self):
        t = np.random.uniform(0, 2*np.pi, self.N)
        x = np.sin(t) + 2*np.sin(2*t)
        y = np.cos(t) - 2*np.cos(2*t)
        z = -np.sin(3*t)
        return x, y, z