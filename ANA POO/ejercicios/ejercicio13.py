def calcular_operaciones_basicas():
    """"Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y
división"""
    num1= float(input("ingrese el primer numero: "))
    num2= float(input("ingrese el segundo numero: "))

    suma = num1 + num2
    resta = num1 - num2
    multiplicar = num1 * num2
    dividir = num1 / num2

    return print( f" el resultado de las operaciones basicas de los numero {num1} y {num2} son : suma = {suma}, resta = {resta}, mltiplicacion = {multiplicar}, dividir = {dividir}")

calcular_operaciones_basicas()