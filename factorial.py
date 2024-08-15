def factorial(n):

    resultado = 1

    for i in range(1, n + 1):

        resultado *= i

    return resultado



numero = int(input("Ingrese el numero a verificar: "))

print("Factorial de", numero, "es:", factorial(numero))