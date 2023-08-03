def calcular_radio():
    """" Escribir una función que calcule el área de un círculo dado su radio"""
    radio = int(input("ingrese el area del circulo: "))
    radio_cuadrado = radio * radio
    pi = 3.14
    area = radio_cuadrado * pi
    return print(area)

calcular_radio()