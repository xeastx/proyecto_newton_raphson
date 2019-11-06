#!/usr/bin/env python3
"""
Proyecto Algoritmo de Newton-Raphson.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

import math

def derivada(f, h = 0.02):
    """
    Retorna la función derivada de f dado un h.

    Parámetros:
    f: función de variable real f(x).
    h: tamaño del paso.
    """

    def _(x):
        return (f(x + h) - f(x))/h

    return _

def newton_raphson(f, x, ER, N):
    """
    Implementa el Algoritmo de Newton-Raphson y retorna la aproximación de la
    raiz.

    Parámetros:
    f: función de variable real f(x).
    x: aproximación inicial.
    ER: cota mínima del error relativo.
    N: número máximo de iteraciones.
    """
    i = 1; err = 1; xi = None
    
    while i <= N and ER < err:
        xi = x - (f(x)/derivada(f, x)(x))
        err = er(x, err)
        print("Iteración:", i, "Aproximación:", xi, "Error:", err)
        i += 1
    return xi


er = lambda a,b: math.fabs((a-b)/a)


if __name__ == "__main__":
    f = lambda x: math.e**x - 3*(x**2)
    print(newton_raphson(f, 1, 0.03, 10))
