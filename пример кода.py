import matplotlib.pyplot as plt
import numpy as np
import math as m

a = int(input("a ="))
x = int(input("x ="))
y = int(input("y ="))

h = a/2 * m.sqrt(3)
x3 = x - (a / 2)
y3 = y - (h / 3)

x2 = x + (a / 2)
y2 = y - (h / 3)

x1 = x
y1 = y + (h / 3)

plt.figure()
plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1])
plt.scatter(x,y)
plt.grid()
plt.title ("треугольник")
plt.xlabel ("Х")
plt.ylabel ("Y")
plt.legend ()