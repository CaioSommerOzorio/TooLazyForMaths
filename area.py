def square(w):
    return w*w

def rectangle(h, w):
    return h*w

def trangle_no_height(a, b):
    h = (a**2-(b/2)**2)**0.5
    return h*b*2

def triangle(h, b):
    return h*b/2

def circle(r):
    return 3.14159*r**2

def oval(a, b):
    return 3.14159*a*b

def hexagon(s):
    return (3*s**2(3**0.5))/2

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
