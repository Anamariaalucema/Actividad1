def calcular_factorial():
    """"Escribir una función que calcule el factorial de un número dado"""
    numero= int(input("ingrese un numero"))
    if numero < 0 :
        return "no esta definido el factorial de un numero negativo"
    else:
        if numero == 0:
            return "el factorial es 1"
        else:
            factorial = 1
            for i in range(1, numero + 1):
                factorial *= i
            return print(factorial)

calcular_factorial()