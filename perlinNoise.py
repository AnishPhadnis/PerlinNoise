from math import floor
import random
from xml.etree.ElementInclude import include
import matplotlib.pyplot as plt


#randomNums = [random.uniform(-1, 1) for i in range(10)]
randomNums = [-0.8472978654485066, 0.9000528285750311, -0.4328894189757624, -0.0055113986838357665, -0.26868175295082874, -0.653747737881957, 0.6808501634140589, -0.2247107373599725, 0.6025352129131027, 0.4042941557771631, -0.18551517480776702]
#print(randomNums)

def getEquationOfLine(slope: int) -> callable:
    def equation(x0:int, x1:int) -> int:
        return slope * (x1-x0) + 0
    
    return equation

randomNumsLine = list(map(getEquationOfLine, randomNums))

positiveValues = list[int]
negativeValues = list[int]
line = list[negativeValues, positiveValues]
# y @ 0, 0.1, ... 1 | 0, -0.1, ...-1

randomSlopeX = []
randomSlopeY = []
incrementVal = 0.1
for i in range(len(randomNums)):
    distanceFromLeftPoint = 0
    
    randomSlopeX.append(i)
    randomSlopeY.append(0)

    for _ in range(int(1/incrementVal)):
        posVal = randomNumsLine[i](i, i+distanceFromLeftPoint)
        randomSlopeX.append(i+distanceFromLeftPoint)
        randomSlopeY.append(posVal)
        
        negVal = randomNumsLine[i](i, i-distanceFromLeftPoint)
        randomSlopeX.append(i-distanceFromLeftPoint)
        randomSlopeY.append(negVal)
        
        #plt.plot(i+distanceFromLeftPoint, posVal, 'bo')
        #plt.plot(i-distanceFromLeftPoint, negVal, 'bo')
        
        distanceFromLeftPoint += incrementVal
        
    #plt.plot(randomSlopeX, randomSlopeY, 'b')
    #plt.plot(i, 0, 'go')
    
    randomSlopeX.clear()
    randomSlopeY.clear()
    
interpolatedX, interpolatedY = [], []
for i in range(1, len(randomNums)):
    increment = -1.0
       
    for j in range(floor(1/incrementVal)+1):
        lastLineY = randomNumsLine[i-1](i-1, i+increment)
        currentLineY = randomNumsLine[i](i, i+increment)
        
        interpolatedVal = lastLineY * abs(increment) + currentLineY * (1-abs(increment))
        
        #plt.plot(i+increment, interpolatedVal, 'ro')
        interpolatedX.append(i+increment)
        interpolatedY.append(interpolatedVal)
        
        increment += 0.1
        
    plt.plot(interpolatedX, interpolatedY, 'r')
        
    #plot point
    plt.plot(i-1, 0, 'go')
    plt.plot(i, 0, 'go')
        
    

#x = [i*incrementVal for i in range((len(randomNums)-1) * int(1/incrementVal)+1)]
#plt.plot(x, interpolated, label='interpolated')

plt.legend()
plt.xlim(-1, 11)
plt.ylim(-1, 1)
plt.show()




