import numpy as np


def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h

def backward_difference(f, x, h):
    return (f(x) - f(x - h)) / h

def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def extrapolated_difference(f, x, h):
    return (8 * f(x + h) - 8 * f(x - h) - f(x + 2 * h) + f(x - 2 * h)) / (12 * h)


