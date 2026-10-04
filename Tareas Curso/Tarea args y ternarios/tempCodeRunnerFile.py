def verificador_cantidad(*args):
    minimo_requerido = 5
    return "Exito" if len(args) >= minimo_requerido else "Error, faltan argumentos"
print(verificador_cantidad(1, 2, 3, 4))