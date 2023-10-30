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

def find_x_ac(a, c):
    return math.degrees(math.asin(a/c))

def find_x_ab(a, b):
    return math.degrees(math.atan(a/b))

def find_x_bc(b, c):
    return math.degrees(math.acos(b/c))

def find_y_ac(a, c):
    return math.degrees(math.acos(a/c))

def find_y_ab(a, b):
    return math.degrees(math.atan(b/a))

def find_y_bc(b, c):
    return math.degrees(math.asin(b/c))
