"""
    Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
    FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
    embargo, también intenta crear el archivo si no existe
"""

try:
    archivo = open("archivo.txt")
except FileNotFoundError:
    # no existe el archivo que se quiere abrir
    print("No existe el archivo que quiere abrirse")