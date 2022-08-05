import functools
import random

class PerlinNoise():
    
    def __init__(self,
                 seed: float = 1,
                 amplitude: float = 1,
                 frequency: float = 0.01,
                 scale: float = 1,
                 octaves: float = 1,
                 persistence: float = 1,
                 lancunarity: float = 1
                 ):
        self.seed = seed
        self.amplitude = amplitude
        self.frequency = frequency
        self.scale = scale 
        self.octaves = octaves 
        self.persistence = persistence 
        self.lancunarity = lancunarity
        
        random.seed(self.seed)
    
    # Extend for higher dimensions
    def get(self, x: float) -> float:
        
        for i in range(self.scale):
            pass
            
        
        pass 
    
    @functools.cache
    def getSlopeAt(self, x: int) -> float:
        return random.uniform(-1 * self.amplitude, self.amplitude)
        
    
    def smootherstep(t: int) -> float:
        return -2*t**3 + 3*t**2
    
    def getInterpolated():
        pass