def imprimir_nombre_edad():
    """" Crear un programa que pida al usuario ingresar su nombre y edad y los imprima en pantalla."""
    nombre = input("ingrese su nombre: ")
    edad = int(input("ingrese su edad: "))
    nombre_edad = f"hola {nombre}, tu edad es {edad}"
    return print(nombre_edad)

imprimir_nombre_edad()
