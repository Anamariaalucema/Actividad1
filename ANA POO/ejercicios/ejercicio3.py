import random
def numeros_aleatorios():
    """" Crear un programa que genere una lista de números aleatorios y los imprima en pantalla."""
    longitud = int(input("de que largo quieres que sea la lista a generar: "))
    lista_aleatoria = [random.randint(1, 10) for _ in range(longitud)]
    return print(lista_aleatoria)

numeros_aleatorios()