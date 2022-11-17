#Ejercicio 6
def inversa(cadena):
    cadenaInvertida = ""

    for i in range(len(cadena)):
        cadenaInvertida += cadena[len(cadena) - i - 1]

    return cadenaInvertida

print(inversa("Macarrones con tomate"))