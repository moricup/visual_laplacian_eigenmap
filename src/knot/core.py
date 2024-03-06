from abc import ABC, abstractmethod

class Sampler(ABC):
    @abstractmethod
    def __init__(self, sample_size):
        pass
    
    @abstractmethod
    def sample(self):
        pass