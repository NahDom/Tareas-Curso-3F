"""
    c. Escribe un programa que intente acceder a una clave que no existe en un
    diccionario. Si se produce una excepción KeyError, captura la excepción y muestra
    un mensaje de error al usuario.
"""

dict = {"nombre": "Nahuel", "edad": 25}

try:
    telefono = dict["telefono"]
    print(f"el telefono es {telefono}")
except KeyError:
    # No se encuentra la clave en el diccionario
    print("No existe la clave telefono en el diccionario")