def cube(a):
    return 6*a**2

def rectangle(w, h, l):
    2*(w*l+h*l+h*w)

# this was a pain
def triangular_prism(a, b, c, h):
    s = (a+b+c)/2
    areab = (s*(s-a)*(s-b)*(s-c))**0.5
    area = 2*areab+(a+b+c)*h
    return area

def sphere(r):
    return 4*3.14159*r**2

# make pull request if you want
