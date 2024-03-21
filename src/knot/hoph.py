import numpy as np

from src.knot.core import Sampler

class HophSampler(Sampler):
    def __init__(self, sample_size):
        self.sample_size = sample_size

    def sample(self):
        t = np.linspace(0, 2*np.pi, int(self.sample_size/2))

        x0 = np.cos(t)
        y0 = np.sin(t)
        z0 = np.zeros_like(t)

        x1 = np.zeros_like(t)
        y1 = np.cos(t) + 1.0
        z1 = np.sin(t)

        x = np.concatenate((x0, x1))
        y = np.concatenate((y0, y1))
        z = np.concatenate((z0, z1))
        return x, y, z