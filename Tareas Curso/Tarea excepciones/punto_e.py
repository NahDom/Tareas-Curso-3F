"""
    e. Escribe un programa que intente dividir dos números. Si el segundo número es cero,
    captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
    captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario
"""
x = 10
y = "hola"
try:
    x = float(x)
    y = int(y)
    resultado = x/y
    print(f"El resultado de la division es: {resultado:.0f}")
except ZeroDivisionError:
    print("No puede dividirse entre cero, intente con otros valores")
except ValueError as e:
    print(f"Ocurrió un error de valor: {e}")