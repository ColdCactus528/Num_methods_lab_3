import matplotlib.pyplot as plt
import numpy as np
import math

def FunctionLab3(x):
    return x * x * math.cosh(3*x)

def IntegrationRectangleMethod(min, maximum, step):
    massY = []
    for i in np.arange(min, maximum, step):
        massY.append(FunctionLab3((i+i+step) / 2) * (i+step - i))

    return sum(massY)

def IntegrationSimpsonMethod(min, maximum, step):
    massY = []
    for i in np.arange(min, maximum, step):
        massY.append((i+step - i) / 6 * (FunctionLab3(i) + 4 * FunctionLab3((i+step + i) / 2) + FunctionLab3(i+step)))

    return sum(massY)

def IntegrationTrapezoidMethod(min, maximum, step):
    massY = []
    for i in np.arange(min, maximum, step):
        massY.append((FunctionLab3(i+step) + FunctionLab3(i)) / 2 * (i+step - i))

    return sum(massY)

def IntegrationGaussian(min, maximum, step):
    massY = []
    for i in np.arange(min, maximum, step):
        massY.append( (i + step - i) / 2 * (FunctionLab3((i + i+step) / 2 - (i+step - i) / (2 * math.sqrt(3))) +
                                              FunctionLab3((i + i+step) / 2 + (i+step - i) / (2 * math.sqrt(3)))))

    return sum(massY)

def LogError(min, maximum, Func):
    step = 0.1
    massErr = []
    massStep = []
    trueIntegral = 3.6881964612475796916294010076613903437852091157617613354535185103
    while(step > 1e-4):
        calculatedIntegral = Func(min, maximum, step)
        massStep.append(math.log(step))
        massErr.append(math.log(abs(trueIntegral - calculatedIntegral)))
        step = step / 10

    return massStep, massErr

step = 0.05
min = -1
maximum = 1
massX = np.linspace(min, maximum, int((maximum - min) / step))
massFunc = [FunctionLab3(i) for i in massX]
massStep, massErr = LogError(min, maximum, IntegrationTrapezoidMethod)
print(str(IntegrationRectangleMethod(min, maximum, step)) + " значение интеграла по методу прямоугольников ")
print(str(IntegrationSimpsonMethod(min, maximum, step)) + " значение интеграла по методу Симпсона ")
print(str(IntegrationTrapezoidMethod(min, maximum, step)) + " значение интеграла по методу трапеций ")
print(str(IntegrationGaussian(min, maximum, step)) + " значение интеграла по методу Гаусса по двум точкам")
plt.title("19 задание")  # заголовок
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
# plt.plot(massX, massFunc, label='функция')
plt.plot(massStep, massErr, label='функция логарифма ошибки')
plt.legend()
plt.show()
