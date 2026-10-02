"""
    b. Escribe un programa que intente sumar un número y una cadena. Si se produce un error
    de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario
"""

try:
    resultado = 10 + "curso 3F"
except TypeError:
    print("¡Error de tipos no puedes sumar un valor y una cadena!")