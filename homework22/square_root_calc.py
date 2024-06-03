# Write a function that calculates the square root of a number using the math module.

from math import sqrt


def sqr_root(inp_num: float) -> float:
    return sqrt(inp_num)


print(sqr_root(8))
