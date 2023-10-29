import matplotlib.pyplot as plt

x_axis = []
y_axis = []
def lin():
    lin_equation = input("Enter your linear equation in the format [a𝑥+b] where a is the coefficient and b is constant: ")
    ran_x = int(input("Enter the range of 𝑥: "))+1
    coef = lin_equation.split('x')[0]
    cons = lin_equation.split('+')[1]
    # table
    for i in range(1, ran_x):
        y = i*int(coef)+int(cons)
        x_axis.append(i)
        y_axis.append(y)

def quadradic():
    a = int(input("Enter a quadradic equation in the format [y=a𝑥^2+bx+c]\na: "))
    b = int(input("b: "))
    c = int(input("c: "))
    min_x = int(input("Enter min x: "))
    max_x = int(input("Enter max x: "))
    for i in range(min_x, max_x+1):
        y = a*i**2+b*i+c
        x_axis.append(i)
        y_axis.append(y)

quadradic()

print(f"x axis: {x_axis}\ny axis: {y_axis}")
plt.ylabel("y")
plt.xlabel("x")
plt.title("Quadradic function")
plt.plot(x_axis, y_axis)
plt.show()