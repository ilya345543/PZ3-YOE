import math
from ex_1 import rescue_nan

@rescue_nan
def op_cube(x):
    return x ** 3

@rescue_nan
def op_square(x):
    return x ** 2

@rescue_nan
def op_disk_area(r):
    return math.pi * r * r

@rescue_nan
def op_sin(x):
    return math.sin(x)

@rescue_nan
def op_cos(x):
    return math.cos(x)

@rescue_nan
def op_abs(x):
    return abs(x)

