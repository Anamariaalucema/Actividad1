def imprimir_numeros():
    """"Crear un programa que imprima los números del 1 al 10 utilizando un ciclo for"""
    lista= []
    numero = 0
    for i in range(1, 11):
        numero = numero + 1
        lista.append(numero)
    return print(lista)

imprimir_numeros()