# how high and low values can go
from noise import PerlinNoise
import matplotlib.pyplot as plt


amplitude = 0 # implemented

# increment of x value where random slope is generated?
frequency = 0 # implemented

# how far zoomed in you are
scale = 0 # implemented?

# how many perlin noise graphs to add for final result
octaves = 0

# how much each successive octave affects final result
persistence = 0

# frequency of successive octaves
lacunarity = 0


perlin1 = PerlinNoise(seed=1, amplitude=10, frequency=1)

x, y1 = [], []
for i in range(10):
    inc = i

    for _ in range(10):
        x.append(inc)
        y1.append(perlin1.getNoiseAt(inc))
        
        inc += 0.1
        
        
#plt.plot(x, y1, 'r')

perlin2 = PerlinNoise(seed=2, amplitude=5, frequency=0.5)

x, y2 = [], []
for i in range(10):
    inc = i

    for _ in range(10):
        x.append(inc)
        y2.append(perlin2.getNoiseAt(inc))
        
        inc += 0.1
        
#plt.plot(x, y2, 'g')

perlin3 = PerlinNoise(seed=3, amplitude=2.5, frequency=0.25)

x, y3 = [], []
for i in range(10):
    inc = i

    for _ in range(10):
        x.append(inc)
        y3.append(perlin3.getNoiseAt(inc))
        
        inc += 0.1
        
#plt.plot(x, y3, 'b')

t = []
for a, b, c in zip(y1, y2, y3):
    t.append(a + c)

plt.plot(x, t, 'y')

perlin4 = PerlinNoise(seed=1, amplitude=10, octaves=1, persistence=0.5, frequency=1, lancunarity=0.5)
x, y4 = [], []

for i in range(10):
    inc = i
    
    for _ in range(10):
        x.append(inc)
        y4.append(perlin4.getNoiseAt(inc))
        
        inc += 0.1
        

#plt.plot(x, y4, 'b')
plt.xlim(-1, 11)
plt.ylim(-10, 10)
plt.show()