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
        return x_axis, y_axis
