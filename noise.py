import functools
import random
import matplotlib.pyplot as plt
import time

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
        
        self.maxVal = -1000
        self.minVal = 1000
        

    
    # Extend for higher dimensions
    def getNoiseAt(self, x: float) -> float:   
        """if x % self.frequency == 0:
            return 0"""
             
        persistenceInc = self.amplitude
        freq = self.frequency
        yVal = 0
        
        """
        are frequencies wrong? just adding y values of different graphs with different frequencies so the line is a bit shaky but there isn't a significant amount of micro features on the line
        """
    
        for octave in range(self.octaves):
            #persistenceInc = 2 ** octave 
            #freq = 2 ** octave
            
            lowerBound: float = int(x // freq) * freq
            upperBound: float = lowerBound + freq
            
            #print(f'{x}: {lowerBound}-{upperBound}')
            
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
            
        self.maxVal = max(yVal, self.maxVal)
        self.minVal = min(yVal, self.minVal)
        
        if self.persistence < 1:
            normalized = 3*self.amplitude * ((yVal - (-1.5)*self.amplitude)/(self.amplitude*1.5-(-1.5)*self.amplitude)) + (-1.5)*self.amplitude
        else:
            normalized = yVal
        
        return normalized
        
    # seed makes it so sequence of random num is always same
    # not that same x val returns same random num
    # no matter what x vals are, sequence of nums will always be same
    @functools.cache
    def getSlopeAt(self, x: float, octave: int) -> float:
        return random.uniform(-1, 1)
        
    
    def smootherstep(self, x: int) -> float:
        return -1 * (-2*x**3 + 3*x**2) + 1
    
    def getInterpolated(self, y1: float, y2: float, adjustment: float) -> float:
        return y1 * adjustment + y2 * (1 - adjustment)
    
    def getY(self, slope: float, x0: float, x1: float) -> float:
        return slope * (x1 - x0)
    
    
perlin = PerlinNoise(
                    seed=1,
                    octaves=8,
                    amplitude=1, persistence=0.5,
                    frequency=2, lancunarity=3
                    )
x, y = [], []

for i in range(50):
    inc = i
    
    for _ in range(1):
        x.append(inc)
        y.append(perlin.getNoiseAt(inc))
        
        inc += 1
#print(x, y)
plt.ion()
#print(y)
#print(perlin.maxVal)
#print(perlin.minVal)
#line = plt.plot(x, y, 'r', linewidth=0.8)
#print(line[0])
plt.xlim(0, 51)
plt.ylim(-3, 3)

#figure, axes = plt.subplots()


inc = 50

for i in range(100000000):
    #time.sleep(0.1)
    plt.pause(0.00001)
    
    x.pop(0)
    x.append(inc)
    
    y.pop(0)
    y.append(perlin.getNoiseAt(inc))
    
    #line[0].set_xdata(x)
    #line[0].set_ydata(y)
    #axes.plot(x, y, 'r')
    plt.xlim(inc-50, inc)
    plt.plot(x, y, 'r')
    
    
    #plt.draw()
    plt.show()
    
    inc += 1
    
    


