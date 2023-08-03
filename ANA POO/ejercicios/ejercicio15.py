def es_palindromo(cadena):
    """"Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no."""
    return cadena == cadena[::-1]

if __name__ == "__main__":
    cadena_ingresada = input("Ingresa una cadena de texto: ")
    if es_palindromo(cadena_ingresada):
      print("La cadena ingresada es un palíndromo.")
    else:
      print("La cadena ingresada no es un palíndromo.")

es_palindromo("hola")