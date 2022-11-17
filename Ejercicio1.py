# Ejercicio 1
def max(num1, num2):
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    else:
        print("Oye, son iguales")
        return None

print(max(2, 2))