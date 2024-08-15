def filtrar_pares(numeros):

    pares = []

    for numero in numeros:

        if numero % 2 == 0:

            pares.append(numero)

    return pares



lista_numeros = [1, 2, 3, 4, 5, 6]
prueba = [1, 2, 3, 4, 5, 6, -1, -2, -3, -4, 0]

print("Números pares:", filtrar_pares(lista_numeros))
print("Números pares:", filtrar_pares(prueba))