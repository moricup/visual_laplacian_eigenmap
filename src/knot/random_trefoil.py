import numpy as np

from src.knot.core import Sampler

class RandomTrefoilSampler(Sampler):
    def __init__(self, sample_size: int):
        self.sample_size = sample_size

    def sample(self, var = 0.15):
        t = np.random.uniform(0, 2*np.pi, self.sample_size)
        x = np.sin(t) + 2*np.sin(2*t) + np.random.normal(0, var, self.sample_size)
        y = np.cos(t) - 2*np.cos(2*t) + np.random.normal(0, var, self.sample_size)
        z = -np.sin(3*t) + np.random.normal(0, var, self.sample_size)
        return x, y, z