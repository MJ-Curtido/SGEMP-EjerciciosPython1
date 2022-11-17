#Ejercicio 3
def calcularLong(lista):
    cont = 0

    for i in lista:
        cont += 1

    return cont

print(calcularLong(["apple", "banana", "cherry"]))