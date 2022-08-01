import random
import matplotlib.pyplot as plt


#randomNums = [random.uniform(-1, 1) for i in range(10)]
randomNums = [-0.8472978654485066, 0.9000528285750311, -0.4328894189757624, -0.0055113986838357665, -0.26868175295082874, -0.653747737881957, 0.6808501634140589, 0.6247107373599725, 0.6025352129131027, 0.4042941557771631, -0.18551517480776702]
#print(randomNums)

def getEquationOfLine(slope: int) -> callable:
    def equation(x0:int, y0:int, x1:int) -> int:
        return slope * (x1-x0) + y0
    
    return equation

randomNumsLine = list(map(getEquationOfLine, randomNums))

interpolated = []
incrementVal = 0.1
for i in range(len(randomNums)):
    distanceFromLeftPoint = 0
    
    for _ in range(int(1/incrementVal)):
        posVal = randomNumsLine[i](i, 0, i+distanceFromLeftPoint)
        negVal = randomNumsLine[i](i, 0, i-distanceFromLeftPoint)
        
        plt.plot(i+distanceFromLeftPoint, posVal, 'bo')
        plt.plot(i-distanceFromLeftPoint, negVal, 'bo')
        
        
        distanceFromLeftPoint += incrementVal
        
    plt.plot(i, 0, 'go')


#x = [i*incrementVal for i in range((len(randomNums)-1) * int(1/incrementVal)+1)]
#plt.plot(x, interpolated, label='interpolated')

plt.legend()
plt.xlim(-1, 11)
plt.ylim(-1, 1)
plt.show()




