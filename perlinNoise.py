import random
import matplotlib.pyplot as plt

#randomNums = [random.uniform(-1, 1) for i in range(10)]
randomNums = [-0.8472978654485066, 0.9000528285750311, -0.4328894189757624, -0.0055113986838357665, -0.26868175295082874, -0.653747737881957, 0.6808501634140589, 0.6247107373599725, 0.6025352129131027, 0.4042941557771631, -0.18551517480776702]
#print(randomNums)

interpolated = []
incrementVal = 0.1
for i in range(len(randomNums)-1):
    print(f'Random num {i}')
    distanceFromLeftPoint = 1.0
    #print('-')
    for _ in range(int(1/incrementVal)):
        #print(distanceFromLeftPoint)
        newVal = randomNums[i] * distanceFromLeftPoint + randomNums[i+1] * (1-distanceFromLeftPoint)
        interpolated.append(newVal)
        distanceFromLeftPoint -= incrementVal
    #print('-')

interpolated.append(randomNums[-1])

#print(len(interpolated))

    

plt.plot([i for i in range(len(randomNums))], randomNums)

x = [i*incrementVal for i in range(len(randomNums) * int(1/incrementVal)+1)]
print(x)
plt.plot(x, interpolated)
plt.show()




