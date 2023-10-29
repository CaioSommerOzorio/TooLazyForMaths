import math
import matplotlib.pyplot as plt

x_axis = []
y_axis = []

def quadradic():
    min_x = int(input("Enter min x: "))
    max_x = int(input("Enter max x: "))
    for i in range(min_x, max_x+1):
        y = math.log(i, 10)
        x_axis.append(i)
        y_axis.append(y)

quadradic()

for i in range(0, len(x_axis)):
    print(f"x: {x_axis[i]}\ny: {y_axis[i]}\n")

plt.ylabel("y")
plt.xlabel("x")
plt.title("Logarithmic function")
plt.plot(x_axis, y_axis)
plt.show()