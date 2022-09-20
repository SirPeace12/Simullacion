import numpy as np
from tabulate import tabulate

class PruebaUnicidadKolmogorov:
    def pruebaKolmogorov(self, arr, largo):
        arr = np.delete(arr, np.s_[2:4], axis=1)

        freAcu = 0
        aux1 = np.array([])
        aux2 = np.array([])
        aux3 = np.array([])
        aux4 = np.array([])

        for x in range(len(arr)):
            freAcu += int(arr[x][1])
            aux1 = np.append(aux1, freAcu)
            aux2 = np.append(aux2, freAcu / largo)
            aux3 = np.append(aux3, (x + 1) / 10)
            aux4 = np.append(aux4, aux3[x] - aux2[x])

        arr = np.insert(arr, 2, aux1, axis=1)
        arr = np.insert(arr, 3, aux2, axis=1)
        arr = np.insert(arr, 4, aux3, axis=1)
        arr = np.insert(arr, 5, abs(aux4), axis=1)

        print('Prueba de Unicidad Komogorov')
        print(tabulate(arr, headers=["rango", "FO", "FOA", "POA", "PEA", "|PEA-POA|"], tablefmt='grid',
                       stralign='center'))

        var = np.max(abs(aux4))
        print("Calculado: " + str(var))

        if (np.max(abs(aux4)) <= 0.043):
            print("Los datos tienen distribucion U(0,1), \npor lo que el generador es bueno en cuanto a uniformidad")
            return True
        else:
            print("No pasó la prueba de Unicidad de Kolmogorov")
            return False