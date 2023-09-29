def separar(lista):
    pares = []
    impares = []

    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    pares.sort()
    impares.sort()

    return pares, impares

numeros = [6, 5, 2, 1, 7]
pares, impares = separar(numeros)
print("Numeros pares:", pares)
print("Numeros impares:", impares)
