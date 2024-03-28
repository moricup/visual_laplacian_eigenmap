import numpy as np

from src.knot.core import Sampler

class HoophSampler(Sampler):
    def __init__(self, sample_size: int):
        self.sample_size = sample_size

    def sample(self):
        t = np.linspace(0, 2*np.pi, int(self.sample_size/3))

        x0 = np.cos(t)
        y0 = np.sin(t)
        z0 = np.zeros_like(t)

        x1 = np.zeros_like(t)
        y1 = np.cos(t) + 1.5
        z1 = np.sin(t)

        x2 = np.cos(t)
        y2 = np.sin(t) + 3.0
        z2 = np.zeros_like(t)

        x = np.concatenate((x0, x1, x2))
        y = np.concatenate((y0, y1, y2))
        z = np.concatenate((z0, z1, z2))
        return x, y, z