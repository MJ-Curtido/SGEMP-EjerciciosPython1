#Ejercicio 8
def superposicion(lista1, lista2):
    comun = False

    for elem in lista1:
        for item in lista2:
            if elem == item:
                comun = True

    return comun

lista1 = {1, 2, 3, 4, 5, 6, 7}
lista2 = {"a", "b", "h", 7, "p"}
print(superposicion(lista1, lista2))