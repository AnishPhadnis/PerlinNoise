from math import floor
import random
import matplotlib.pyplot as plt

incrementVal = 0.01
numberOfPoints = 20
slopeIncrement = 0.5

randomNums = [random.uniform(-1, 1) for i in range(numberOfPoints)]
#randomNums = [-0.8472978654485066, 0.9000528285750311, -0.4328894189757624, -0.0055113986838357665, -0.26868175295082874, -0.653747737881957, 0.6808501634140589, -0.2247107373599725, 0.6025352129131027, 0.4042941557771631, -0.18551517480776702]
#print(randomNums)

def smootherstep(t: int) -> float:
    if t == 0:
        return 0
    elif t == 1:
        return 1
    else:
        return -2*t**3 + 3*t**2

def getEquationOfLine(slope: int) -> callable:
    def equation(x0:int, x1:int) -> int:
        return slope * (x1-x0) + 0
    
    return equation

def getInterpolatedVal(equation: int, x: float, increment: float,  adjustment: float) -> float:
    lastLineY = randomNumsLine[equation-1](x-slopeIncrement, x+increment)
    currentLineY = randomNumsLine[equation](x, x+increment)
        
    interpolatedVal = lastLineY * adjustment + currentLineY * (1-adjustment)
    
    return interpolatedVal

randomNumsLine = list(map(getEquationOfLine, randomNums))


randomSlopeX = []
randomSlopeY = []
for i in range(len(randomNums)):
    distanceFromLeftPoint = 0
    
    x = i * slopeIncrement
    
    randomSlopeX.append(x)
    randomSlopeY.append(0)

    for _ in range(int(1/incrementVal)):
        posVal = randomNumsLine[i](x, x+distanceFromLeftPoint)
        randomSlopeX.append(x+distanceFromLeftPoint)
        randomSlopeY.append(posVal)
        
        negVal = randomNumsLine[i](x, x-distanceFromLeftPoint)
        randomSlopeX.append(x-distanceFromLeftPoint)
        randomSlopeY.append(negVal)
        
        distanceFromLeftPoint += incrementVal
        
    plt.plot(randomSlopeX, randomSlopeY, 'b')
    
    randomSlopeX.clear()
    randomSlopeY.clear()
    
    
for i in range(len(randomNums)):
    x = i * slopeIncrement
    
    if i == 0:
        plt.plot(x, 0, 'go')
        continue
    
    xVals, interpolatedY = [], []
    smoothersteppedX, smoothersteppedY = [], []
    
    increment = -1 * slopeIncrement
    for _ in range(floor(slopeIncrement/incrementVal)+1):
        interpolatedVal = getInterpolatedVal(i, x, increment, abs(increment/slopeIncrement))

        xVals.append(x+increment)
        interpolatedY.append(interpolatedVal)
        
        # ------
        
        smootherstepped = smootherstep(abs(increment/slopeIncrement))
        
        smootherstepInterpolated = getInterpolatedVal(i, x, increment, smootherstepped)
        
        smoothersteppedX.append(x+increment)
        smoothersteppedY.append(smootherstepInterpolated)
        
        # ------
        
        increment += incrementVal
        
    plt.plot(xVals, interpolatedY, 'r')
    plt.plot(smoothersteppedX, smoothersteppedY, 'y')
        
    plt.plot(x, 0, 'go')
        

plt.legend()
plt.xlim(-1, numberOfPoints*slopeIncrement+1)
plt.ylim(-1, 1)
plt.show()




