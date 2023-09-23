mail = input("Ingrese un mail: ")
cantidad = 0
x = 0

while x <= len(mail):
    if mail[x] == "@":
        cantidad += 1
        x += 1
    if cantidad == 1:
        print("Contiene un solo caracter @ el mail ingresado")
        break
    else:
        print("Incorrecto")
        break
