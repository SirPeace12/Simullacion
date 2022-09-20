from tabulate import tabulate
import math
import numpy as np
from PruebaUniChi import *
from PruebaUnicidadKolmogorov import *
from pruebaCorrido import *

def genLinCongruente(xo,x,a,c,m):
    xn=0
    i=0
    guardados = np.array([])
    salida = []

    aux =0
    while xn != x:
        xn = (a * xo + c) % m
        rn = xn / m
        xo=xn
        i+=1
        guardados = np.append(guardados,[rn])
        salida.append([i,xn, rn])
        aux+=1

    print(tabulate(salida, headers=["index","Xn", "Rn"],tablefmt='grid',stralign='center'))

    chi=PruebaUniChi()
    frecuencias=chi.pruChi(guardados)

    kolmogorov = PruebaUnicidadKolmogorov()
    kolmogorov.pruebaKolmogorov(frecuencias, len(guardados))

def genEstandarMinimo(xo,x,a,m):
    xn=0
    i=0
    salida=[]
    q=math.floor(m/a)
    r=m % a
    mn=(a*q)+r

    #print (xn)
    while xn!=x:
        xn = a*(xo % q) - r * math.floor(xo/q)
        if(xn >= 0):
            xo=xn
            rn= xn/mn
            i+=1
            salida.append([i, xo, rn])
            print(xn)
        else:
            #xn = a * (xn % q) - r * math.floor(xn / q) + mn
            xn = xn + mn
            xo = xn
            rn = xn / mn
            i += 1
            salida.append([i, xo, rn])
            #print("sumando m")
            #print(xn)
    print(tabulate(salida, headers=["index", "Xn", "Rn"],tablefmt='grid',stralign='center'))
    #print(xn)


if __name__ == '__main__':

    print("Ingresar Xo, a, c y m")

    xo = int(input("Xo: "))
    a = int(input("a: " ))
    c = int(input("c: "))
    m = int(input("m: "))

    #genLinCongruente(xo,xo,a,c,m)
    #genEstandarMinimo(xo,xo,a,m)

    #----------------
    #pruebas de independdencia
    prueba = np.array([0.08, 0.09, 0.23, 0.29, 0.42, 0.55, 0.58, 0.72, 0.89, 0.91,
                       0.11, 0.16, 0.18, 0.31, 0.41, 0.53, 0.71, 0.73, 0.74, 0.84,
                       0.01, 0.09, 0.30, 0.32, 0.45, 0.47, 0.69, 0.74, 0.91, 0.95,
                       0.12, 0.13, 0.29, 0.36, 0.38, 0.54, 0.68, 0.86, 0.88, 0.91])

    prueba2 = np.array([0.41, 0.68, 0.89, 0.94, 0.74, 0.91, 0.55, 0.62, 0.36, 0.27,
                        0.19, 0.72, 0.75, 0.08, 0.54, 0.02, 0.01, 0.36, 0.16, 0.28,
                        0.18, 0.01, 0.95, 0.69, 0.18, 0.47, 0.23, 0.32, 0.82, 0.53,
                        0.31, 0.42, 0.73, 0.04, 0.83, 0.45, 0.13, 0.57, 0.63, 0.29,
                        ])

    pCorrido = pruebaCorrido()
    pCorrido.corrido(prueba2)
