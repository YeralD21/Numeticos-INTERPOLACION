import numpy as np
import scipy.interpolate as spi
from numpy.polynomial.polynomial import Polynomial
from scipy.interpolate import CubicSpline

# Método de Lagrange
def lagrange_interpolation(x, y, xi):
    n = len(x)
    yi = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term = term * (xi - x[j]) / (x[i] - x[j])
        yi += term
    return yi

# Diferencias Divididas de Newton
def newton_divided_diff(x, y, xi):
    n = len(x)
    coef = np.zeros([n, n])
    coef[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])

    yi = coef[0, 0]
    for i in range(1, n):
        term = coef[0, i]
        for j in range(i):
            term = term * (xi - x[j])
        yi += term
    return yi

# Ajuste por Mínimos Cuadrados (Regresión Lineal)
def least_squares_linear(x, y):
    p = np.polyfit(x, y, 1)
    return Polynomial(p)

# Ajuste por Mínimos Cuadrados (Regresión Polinómica)
def least_squares_polynomial(x, y, degree):
    p = np.polyfit(x, y, degree)
    return Polynomial(p)

# Spline Cúbico
def cubic_spline_interpolation(x, y, xi):
    cs = CubicSpline(x, y)
    return cs(xi)
