cadena_usuario = input("Escriba una cadena de texto: ")

cadena_usuario = cadena_usuario.lower()

cadena_usuario = cadena_usuario.replace(" ", "")

cadena_invertida = ""
for caracter in cadena_usuario:
    cadena_invertida = caracter + cadena_invertida

if cadena_usuario == cadena_invertida:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
