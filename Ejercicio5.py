#Ejercicio 5
def sum(lista):
    solucion = 0

    for i in lista:
        solucion += i

    return solucion

print(sum([7, 5, 8, 3, 8, 0, 9, 7]))

def multip(lista):
    solucion = 1

    for i in lista:
        solucion *= i

    return solucion

print(multip([7, 5, 8, 3, 8, 1, 9, 7]))