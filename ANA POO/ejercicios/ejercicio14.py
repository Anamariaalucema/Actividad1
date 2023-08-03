def calcular_media_aritmetica():
    """"Escribir una función que calcule la media aritmética de una lista de números."""
    lista = [3, 4, 6, 1]
    longitud = len(lista)
    if longitud == 0:
        return "la lista esta vasia, no se puede calcular la media aritmetica"
    else:
        suma = 0
        for elemento in lista:
            suma = suma + elemento

        resultado = suma / longitud
        return print(resultado)

calcular_media_aritmetica()