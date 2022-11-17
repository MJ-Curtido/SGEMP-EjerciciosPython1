#Ejercicio 9
def generarNCaracteres(num, caracter):
    cont = 0
    cadena = ""

    while cont < num:
        cadena += caracter
        cont += 1

    return cadena

print(generarNCaracteres(7, "p"))