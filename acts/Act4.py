"""Actividad 4
Escribir un programa que almacene la cadena de caracteres 12345EDD como
contraseña. En una variable, pregunte al usuario por la contraseña hasta que
introduzca la contraseña correcta."""

contraseña = "12345EDD"

print("introduzca su contraseña")

codigo = input()

while contraseña != codigo:
    codigo = input("Contraseña Incorrecta, intentelo de nuevo: ")

print("Acceso conseguido")

