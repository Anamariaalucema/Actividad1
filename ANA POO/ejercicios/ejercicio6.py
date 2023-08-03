def suma_elementos_lista():
    """"Crear un programa que calcule la suma de los números en una lista dada."""
    lista = [5, 4, 3, 1, 9]
    suma = 0
    for elemento in lista:
        suma = suma + elemento
    return print(suma)

suma_elementos_lista()