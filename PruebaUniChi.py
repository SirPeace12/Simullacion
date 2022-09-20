import numpy as np
from tabulate import tabulate
class PruebaUniChi:
    def pruChi(self, arr):
        self.arr = arr
        x1 = 0
        x2 = 0
        x3 = 0
        x4 = 0
        x5 = 0
        x6 = 0
        x7 = 0
        x8 = 0
        x9 = 0
        x10 = 0

        fe = len(arr) / 10

        for x in arr:
            if (x >= 0 and x < 0.1):
                x1 += 1

            if (x >= 0.1 and x < 0.2):
                x2 += 1

            if (x >= 0.2 and x < 0.3):
                x3 += 1

            if (x >= 0.3 and x < 0.4):
                x4 += 1

            if (x >= 0.4 and x < 0.5):
                x5 += 1

            if (x >= 0.5 and x < 0.6):
                x6 += 1

            if (x >= 0.6 and x < 0.7):
                x7 += 1

            if (x >= 0.7 and x < 0.8):
                x8 += 1

            if (x >= 0.8 and x < 0.9):
                x9 += 1

            if (x >= 0.9 and x < 1):
                x10 += 1

        frecuencias = np.array([['0-0.1', x1, fe, (fe - x1) ** 2 / fe]])
        frecuencias = np.vstack([frecuencias, ['0.1-0.2', x2, fe, (fe - x2) ** 2 / fe]])
        frecuencias = np.vstack([frecuencias, ['0.2-0.3', x3, fe, (fe - x3) ** 2 / fe]])
        frecuencias = np.vstack([frecuencias, ['0.3-0.4', x4, fe, (fe - x4) ** 2 / fe]])
        frecuencias = np.vstack([frecuencias, ['0.4-0.5', x5, fe, (fe - x5) ** 2 / fe]])
        frecuencias = np.vstack([frecuencias, ['0.5-0.6', x6, fe, (fe - x6) ** 2 / fe]])
        frecuencias = np.vstack([frecuencias, ['0.6-0.7', x7, fe, (fe - x7) ** 2 / fe]])
        frecuencias = np.vstack([frecuencias, ['0.7-0.8', x8, fe, (fe - x8) ** 2 / fe]])
        frecuencias = np.vstack([frecuencias, ['0.8-0.9', x9, fe, (fe - x9) ** 2 / fe]])
        frecuencias = np.vstack([frecuencias, ['0.9-1', x10, fe, (fe - x10) ** 2 / fe]])

        print('Prueba de Unicidad X^2')

        print(
            tabulate(frecuencias, headers=["rango", "FO", "FE", "(FE - FO)^2/FE"], tablefmt='grid', stralign='center'))

        xCalc = 0
        for i in range(len(frecuencias)):
            xCalc += float(frecuencias[i][3])

        print("Calculado: " + str(xCalc))

        if (xCalc <= 16.92):
            print("Los datos tienen distribucion U(0,1), \npor lo que el generador es bueno en cuanto a uniformidad")

            return frecuencias
        else:
            print("No pasó la prueba de Unicidad de X^2")