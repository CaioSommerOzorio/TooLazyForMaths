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

lin()

print(f"x axis: {x_axis}\ny axis: {y_axis}")
plt.ylabel("y")
plt.xlabel("x")
plt.title("Linear equation")
plt.plot(x_axis, y_axis)
plt.show()
