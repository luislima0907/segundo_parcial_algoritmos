#Calcular el promedio de una lista con los datos que ingrese el usuario
def suma_promedio_de_una_lista():
    numero_ingresado = int(input("Ingrese un numero \n"))
    suma = 0
    contador = 0
    while numero_ingresado > 0:
        suma += numero_ingresado
        contador += 1
        numero_ingresado = int(input("Ingrese un numero \n"))
    print(f"La suma es {suma}")
    print(f"El promedio es {suma/contador}")
suma_promedio_de_una_lista()
