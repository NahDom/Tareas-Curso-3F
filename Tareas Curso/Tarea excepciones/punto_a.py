"""
    a. Escribe un programa que intente dividir dos números. Si el segundo número es cero,
    captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario
"""
x = 10
y = 0
try:
    resultado = x/y
    print(f"El resultado de la division es: {resultado:.0f}")
except ZeroDivisionError:
    print("No puede dividirse entre cero, intente con otros valores")