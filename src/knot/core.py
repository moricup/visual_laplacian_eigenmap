from abc import ABC, abstractmethod

class Sampler(ABC):
    @abstractmethod
    def __init__(self, N):
        pass
    
    @abstractmethod
    def sample(self):
        pass