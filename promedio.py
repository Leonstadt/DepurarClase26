def calcular_promedio(numeros):

    suma = 0

    for numero in numeros:

        suma += numero
    if len(numeros) == 0:
        return "Lista vacia"
    
    elif len(numeros) > 0:
        promedio = suma / len(numeros)
        return promedio
    
    



lista_numeros = [10, 20, 30, 40, 50]
lista_vacia=[]

print("El promedio es:", calcular_promedio(lista_numeros))
print("El promedio es:", calcular_promedio(lista_vacia))