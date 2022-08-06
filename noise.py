import functools
import random

class PerlinNoise():
    
    def __init__(self,
                 seed: float = 1,
                 amplitude: float = 1,
                 frequency: float = 1,
                 scale: float = 1,
                 octaves: float = 1,
                 persistence: float = 1,
                 lancunarity: float = 1
                 ):
        self.seed = seed # used
        self.amplitude = amplitude # used
        self.frequency = frequency
        self.scale = scale 
        self.octaves = octaves 
        self.persistence = persistence 
        self.lancunarity = lancunarity
        
        random.seed(self.seed)
    
    # Extend for higher dimensions
    def getNoiseAt(self, x: float) -> float:
        if x % self.frequency == 0:
            print(f'{x}')
            return 0
        
        lowerBound: int = int(x // self.frequency) * self.frequency
        upperBound: int = lowerBound + self.frequency
        
        distanceToLowerBound: float = x - lowerBound
        
        lowerBoundSlope: float = self.getSlopeAt(lowerBound)
        upperBoundSlope: float = self.getSlopeAt(upperBound)
        
        smoothersteppedDiff: float = self.smootherstep(distanceToLowerBound)
        
        yVal: float = self.getInterpolated(self.getY(lowerBoundSlope, lowerBound, x),
                                           self.getY(upperBoundSlope, upperBound, x), smoothersteppedDiff
                                           )
        
        print(f'{x}={lowerBound}-{upperBound} w/ {lowerBoundSlope}-{upperBoundSlope} -> {distanceToLowerBound}-{smoothersteppedDiff} -> {yVal}')
        return yVal
        
    # seed makes it so sequence of random num is always same
    # not that same x val returns same random num
    # no matter what x vals are, sequence of nums will always be same
    @functools.cache
    def getSlopeAt(self, x: int, octave: int) -> float:
        return random.uniform(-1 * self.amplitude, self.amplitude)
        
    
    def smootherstep(self, x: int) -> float:
        return -1 * (-2*x**3 + 3*x**2) + 1
    
    def getInterpolated(self, y1: float, y2: float, adjustment: float) -> float:
        return y1 * adjustment + y2 * (self.frequency - adjustment)
    
    def getY(self, slope: float, x0: float, x1: float) -> float:
        return slope * (x1 - x0)
    
    
