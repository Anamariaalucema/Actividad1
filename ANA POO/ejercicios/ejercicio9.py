import random
def imprimir_matriz():
    """"Crear un programa que genere una matriz de números y la imprima en pantalla."""
    columnas = int(input("cuantas columnas quiere que tenga la matriz: "))
    filas = int(input("cuantas filas quiere que tenga la matriz: "))
    matriz = [[random.randint(1, 100)for _ in range(columnas)] for _ in range(filas)]
    return print(matriz)

imprimir_matriz()