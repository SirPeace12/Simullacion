
import numpy as np
import math as mt

class pruebaCorrido:

    def corrido(self, arr):
        n=len(arr)
        simbolos = np.array([])
        cantCorridas = 1

        for x in range(len(arr)):
            if (x == 0):
                simbolos = np.append(simbolos, "*")

            else:
                if (arr[x - 1] <= arr[x]):
                    simbolos = np.append(simbolos, "+")
                else:
                    simbolos = np.append(simbolos, "-")

            if (simbolos[x] != simbolos[x - 1] and x != 1):
                cantCorridas += 1

        print(arr)
        print("\n")
        print(simbolos)
        print(cantCorridas)

        media =  ((2*n)-1)/3
        varianza = ((16*n)-29)/90
        zObs = (cantCorridas-media)/mt.sqrt(varianza)
        print("Z Obtenido: " + str(zObs))
        if(zObs>= -1.96 and zObs<= 1.96 ):
            print("No hay evidencia para rechazar la hipotesis de independencia")
        else:
            print("No pasa las pruebas de independencia.")