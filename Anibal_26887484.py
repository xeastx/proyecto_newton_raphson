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
    Ea=ER+1     #Error Relativo Actual
    i=1         #Numero de Iteracion
    xi=0        #Aproximacion actual
    while ( (Ea>ER) & (N>i) ):
        fd=derivada(f)           #Se calcula la derivada de la funcion
        xi = x - ( f(x) / fd(x) )           #Se calcula el punto siguiente 
        Ea= abs( ( xi - x ) / xi)           #Se calcula el Error relativo Actual
        if(i>1):                            #Se evalua que se va a mostrar por pantalla
            print("Iteración:", i, "Aproximación:", xi, "Error:", Ea)
        else:
            print("Iteracion:",i,"Aproximacion:",xi)
        x=xi       #Se asigna el nuevo punto anterior
        i+=1
    return xi

f1 = lambda x: math.exp(x) - ( 3 * pow(x,2))    #Primera funcion de Clase con xi=0.5 y er=0.02
f2 = lambda x: math.sin(x) - math.exp(-x)       #Segunda Funcion de Clase con xi=3.5 y er=0.035
f3 = lambda x: math.exp(-x) - math.log(x)       #Primer ejemplo de la guia con xi=1 y er=0.01

if __name__ == "__main__":
    print ("El ultimo valor de Xi es: ",newton_raphson(f1, 0.5, 0.02, 10))
