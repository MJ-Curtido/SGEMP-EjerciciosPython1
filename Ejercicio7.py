#Ejercicio 7
def isPalindromo(cadena):
    cadena.lower()

    if cadena == cadena[::-1]:
        return True
    else:
        return False

print(isPalindromo("parguela"))