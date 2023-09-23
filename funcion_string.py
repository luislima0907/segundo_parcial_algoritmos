#Escribir un programa que encuentre una letra dentro de una string  y decir cuantas veces se encuentra
#Puede ser en mayusculas o minusculas 

string_del_usuario = input("Escriba una frase, puede ser en mayusculas o minusculas \n")
letra_a_encontrar = input("Ingrese una letra que quiera encontrar dentro de la string \n")

def encontrar_cuantas_veces_esta_una_letra():
    veces_que_encuentra_una_letra = string_del_usuario.count(letra_a_encontrar)
    print(f"La letra se encontro {veces_que_encuentra_una_letra}")    
encontrar_cuantas_veces_esta_una_letra()