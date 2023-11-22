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

# returns length of a

def find_a_xb(x, b):
    return b*math.tan(x)

def find_a_xc(x, c):
    return c*math.sin(x)

def find_a_yb(y, b):
    return b/math.tan(y)

def find_a_yc(y, c):
    return c*math.cos(y)

# returns length of b

def find_b_xa(x, a):
    return a/math.tan(x)

def find_b_xc(x, c):
    return c/math.cos(x)

def find_b_ya(y, a):
    return a*math.tan(y)

def find_b_yc(y, c):
    return c*math.sin(y)

# returns length of c

def find_c_xa(x, a):
    return a/math.sin(x)

def find_c_xb(x, b):
    return b/math.cos(x)

def find_c_ya(y, a):
    return a/math.cos(y)

def find_c_yb(y, b):
    return b/math.sin(y)
