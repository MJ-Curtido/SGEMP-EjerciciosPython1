#Ejercicio 10
def procedimiento(lista):
    cadena = ""

    for elem in lista:
        cont = 0

        while cont < elem:
            cadena += "*"
            cont += 1

        cadena += "\n"

    return cadena

print(procedimiento([7, 5, 2, 9]))