#
#   │╲
#   │y╲
#   │  ╲ 
#   │   ╲
# a │    ╲ c
#   │     ╲
#   │      ╲
#   ├┐     x╲
#   └┴───────┘
#        b

import math
import matplotlib.pyplot as plt

# returns length of a

def find_a_xb(x, b):
    return b*math.tan(math.radians(x))

def find_a_xc(x, c):
    return c/math.sin(math.radians(x))

def find_a_yb(y, b):
    return b/math.tan(math.radians(y))

def find_a_yc(y, c):
    return c*math.cos(math.radians(y))

# returns length of b

def find_b_xa(x, a):
    return a/math.tan(math.radians(x))

def find_b_xc(x, c):
    return c*math.cos(math.radians(x))

def find_b_ya(y, a):
    return a*math.tan(math.radians(y))

def find_b_yc(y, c):
    return c*math.sin(math.radians(y))

# returns length of c

def find_c_xa(x, a):
    return a/math.sin(math.radians(x))

def find_c_xb(x, b):
    return b/math.cos(math.radians(x))

def find_c_ya(y, a):
    return a/math.cos(math.radians(y))

def find_c_yb(y, b):
    return b/math.sin(math.radians(y))

def find_a(b, c):
  return (c**2-b**2)**0.5

def find_b(a, c):
  return (c**2-a**2)**0.5

def find_c(a, b):
  return (a**2+b**2)**0.5

def square(w):
    return w*w 

def rectangle(h, w):
    return h*w

def triangle(h, b):
    return h*b/2

def trangle_no_height(a, b):
    h = (a**2-(b/2)**2)**0.5
    return h*b*2

def circle(r):
    return 3.14159*r**2

def oval(a, b):
    return 3.14159*a*b

def hexagon(s):
    return (3*s**2*(3**0.5))/2

def parallelogram(b, h):
    return b*h

def parallelogram_no_height(a, b):
    h = (b**2+a**2)**0.5
    return b*h

def trapezium(a, b, h):
    return (a+b)/2*h

def kite(p, q):
    return p*q/2

def pentagon(a):
    return (1/4)*(5*(5+2*5**0.5)**0.5)*a**2

def cube(w):
    return w**3

def rectangular_prism(w, h, l):
    return w*h*l

def triangular_prism(b, h, l):
    a = h*b/2
    return a*l

def triangular_prism_no_height(b, a, l):
    h = (a**2-b/2**2)**0.5
    return h*b/2*l

def sphere(r):
    return (4/3)*3.14159*r**3

def cylinder(r, h):
    3.14159*r**2*h

def ellipsoid(a, b, c):
    (4/3)*3.14159*a*b*c

def cone(r, h):
    return 3.14159*r**2*(h/3)

def pyramid_rectangular_base(l, w, h):
    (l*w*h)/3

def pyramid_triangular_base(a, h):
    pass
    # not yet

def trapezoidal_prism(a, b, h, l):
    return ((a+b)/2*h)*l

def distance(x1, x2, y1, y2):
	x3 = int(x1) - int(x2)
	y3 = int(y1) - int(y2)
	x3 = x3**2
	y3 = y3**2
	distance = (x3+y3)**0.5
	return distance

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

def midpoint():
	x1 = input("Enter x1: ")
	x2 = input("Enter x2: ")
	y1 = input("Enter y1: ")
	y2 = input("Enter y2: ")
	x3 = int(x1)+int(x2)
	y3 = int(y1)+int(y2)
	return f"({int(x3)/2}, {int(y3)/2})"

def quadradic():
    min_x = int(input("Enter min x: "))
    max_x = int(input("Enter max x: "))
    for i in range(min_x, max_x+1):
        y = math.log(i, 10)
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

