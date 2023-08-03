import random
def lista_numeros_pares():
    """"Crear un programa que genere una lista de números pares entre 1 y 100"""
    longitud = int(input("de que largo quieres que sea la lista a generar: "))
    lista_aleatoria = [random.randint(1, 100) for _ in range(longitud)]

    lista_pares= []
    for elemento in lista_aleatoria:
        if elemento % 2 == 0:
            lista_pares.append(elemento)
        else:
            del(elemento)

    return print(lista_pares)

lista_numeros_pares()