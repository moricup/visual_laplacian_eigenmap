import numpy as np

from src.knot.core import Sampler

class EightSampler(Sampler):
    def __init__(self, sample_size: int):
        self.sample_size = sample_size

    def sample(self):
        t = np.linspace(0, 2*np.pi, self.sample_size)
        x = (2 + np.cos(2*t)) * np.cos(3*t)
        y = (2 + np.cos(2*t)) * np.sin(3*t)
        z = np.sin(4*t)
        return x, y, z