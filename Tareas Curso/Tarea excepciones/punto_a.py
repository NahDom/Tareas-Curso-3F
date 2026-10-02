"""
    a. Escribe un programa que intente dividir dos números. Si el segundo número es cero,
    captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario
"""

def division_entre_dos_numeros(x,y):
    try:
        resultado = x/y
        return f"El resultado de la division es: {resultado:.2f}"
    except ZeroDivisionError:
        return "No puede dividirse entre cero, intente con otros valores"
    
def division():
    x = int(input("Ingrese el primer valor: "))
    y = int(input("Ingrese el segundo valor: "))
    return division_entre_dos_numeros(x,y)

print(division())