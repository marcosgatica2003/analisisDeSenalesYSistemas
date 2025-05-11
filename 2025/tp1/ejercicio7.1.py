import math
import pandas as pd 
import matplotlib.pyplot as plt 

def f(x):
    return 3 / (3 - 2*math.cos(x) + math.sin(x))

xVals = [] 
yVals = []
n = 200
a = 0
b = 2 * math.pi

for i in range (n+1):
    x = a + (b - a) * i/n
    y = f(x)
    xVals.append(x)
    yVals.append(y)

df = pd.DataFrame({'x': xVals, 'y': yVals}) 
df.plot(x='x', y='y', kind='line', legend=False, title='Área bajo la curva f(x)', color='blue')
plt.fill_between(df['x'], df['y'], color='skyblue', alpha=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
