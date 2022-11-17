# Ejercicio 2
def max_de_tres(num1, num2, num3):
    lista = [num1, num2, num3]
    lista.sort()
    lista.reverse()
    return lista[0]

print(max_de_tres(2, 4, 3))