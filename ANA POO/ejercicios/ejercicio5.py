def convertir_grados():
    """"Crear una función que convierta grados Fahrenheit a grados Celsius."""
    grados = int(input("ingrese los grados que desea convertir: "))
    convertir = (grados-32) * 5/9
    return print(f"en grados celsius, los grados {grados} fahrenheit son {convertir} celsius")

convertir_grados()