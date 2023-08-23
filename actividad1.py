def sumar_lista(lista_inventada):
    suma = 0
    for numero in lista_inventada:
        suma += numero
    return suma

# Ejemplo de aplicación del programa
mi_lista = [1, 2, 3, 4, 5, 6, 7]
resultado = sumar_lista(mi_lista)
print("La suma de la lista es:", resultado)