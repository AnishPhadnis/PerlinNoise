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

perlin = PerlinNoise(amplitude=10)

x, y = [], []
for i in range(10):
    inc = i
    for _ in range(10):
        x.append(inc)
        y.append(perlin.getNoiseAt(inc))
        
        inc += 0.1


plt.plot(x, y, 'y')
plt.xlim(-1, 11)
plt.ylim(-10, 10)
plt.show()