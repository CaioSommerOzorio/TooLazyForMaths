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
