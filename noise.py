import functools
import random
import matplotlib.pyplot as plt

class PerlinNoise():
    
    def __init__(self,
                 seed: float = 1,
                 amplitude: float = 1,
                 frequency: float = 1,
                 scale: float = 1,
                 octaves: float = 1,
                 persistence: float = 0.5,
                 lancunarity: float = 0.5
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
        persistenceInc = self.amplitude
        freq = self.frequency
        yVal = 0
        
        """
        are frequencies wrong? just adding y values of different graphs with different frequencies so the line is a bit shaky but there isn't a significant amount of micro features on the line
        """
    
        for octave in range(self.octaves):
            lowerBound: float = int(x // freq) * freq
            upperBound: float = lowerBound + freq
            
            print(f'{x}: {lowerBound}-{upperBound}')
            
            distanceToLowerBound: float = x - lowerBound
            
            smoothersteppedDiff: float = self.smootherstep(distanceToLowerBound / freq)
            
            lowerBoundSlope: float = self.getSlopeAt(lowerBound, octave) * persistenceInc
            upperBoundSlope: float = self.getSlopeAt(upperBound, octave) * persistenceInc
        
        
            result: float = self.getInterpolated(self.getY(lowerBoundSlope, lowerBound, x),
                                                 self.getY(upperBoundSlope, upperBound, x),
                                                 smoothersteppedDiff
                                                 )

            yVal += result 
            
            persistenceInc *= self.persistence
            freq *= self.lancunarity
        
        return yVal
        
    # seed makes it so sequence of random num is always same
    # not that same x val returns same random num
    # no matter what x vals are, sequence of nums will always be same
    @functools.cache
    def getSlopeAt(self, x: int, octave: int) -> float:
        return random.uniform(-1, 1)
        
    
    def smootherstep(self, x: int) -> float:
        return -1 * (-2*x**3 + 3*x**2) + 1
    
    def getInterpolated(self, y1: float, y2: float, adjustment: float) -> float:
        return y1 * adjustment + y2 * (1 - adjustment)
    
    def getY(self, slope: float, x0: float, x1: float) -> float:
        return slope * (x1 - x0)
    
    
perlin4 = PerlinNoise(seed=2,
                      octaves=6,
                      amplitude=10,persistence=0.5,
                      frequency=0.5, lancunarity=0.5)
x, y4 = [], []

for i in range(1):
    inc = i
    
    for _ in range(1000):
        x.append(inc)
        y4.append(perlin4.getNoiseAt(inc))
        
        inc += 0.001
        

plt.plot(x, y4, 'r', linewidth=0.3)
plt.xlim(0, 1)
plt.ylim(-11, 11)
plt.show()