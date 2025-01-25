import numpy as np
import matplotlib.pyplot as plt


def euler_method(func, point, h, stop):
    x0, y0 = point
    n = int((stop - x0) / h)
    xs = [x0]
    ys = [y0]
    x, y = x0, y0
    for i in range(n):
        y_new = y + h * func(x, y)
        x = x + h
        y = y_new
        xs.append(x)
        ys.append(y)
    return xs, ys


def runge_kutta_2nd_order(func, point, h, stop):
    x0, y0 = point
    n = int((stop - x0) / h)
    xs = [x0]
    ys = [y0]
    x, y = x0, y0
    for i in range(n):
        k1 = h * func(x, y)
        y_new = y + h * func(x + 0.5 * h, y + 0.5 * k1)
        x = x + h
        y = y_new
        xs.append(x)
        ys.append(y)
    return xs, ys


def runge_kutta_4rd_order(func, point, h, stop):
    x0, y0 = point
    n = int((stop - x0) / h)
    xs = [x0]
    ys = [y0]
    x, y = x0, y0
    for i in range(n):
        k1 = h * func(x, y)
        k2 = h * func(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * func(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * func(x + h, y + k3)
        dy = 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        y_new = y + dy
        x = x + h
        y = y_new
        xs.append(x)
        ys.append(y)
    return xs, ys

