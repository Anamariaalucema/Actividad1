def def_numero_par_impar():
    """"Escribir un programa que determine si un número dado es par o impar"""
    numero = int(input("ingresa un numero entero: "))
    if numero % 2 == 0:
        return print(f"el numero {numero} es par")
    else:
        return print(f"el numero {numero} es impar")

def_numero_par_impar()