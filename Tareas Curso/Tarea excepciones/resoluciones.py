
print("==============================================================================") 
print("Ejercicios del punto a al e")
print("==============================================================================") 
x = 10
y = 0
try:
    resultado = x/y
    print(f"El resultado de la division es: {resultado:.0f}")
except ZeroDivisionError:
    print("No puede dividirse entre cero, intente con otros valores")
print("==============================================================================")
try:
    resultado = 10 + "curso 3F"
except TypeError:
    print("¡Error de tipos no puedes sumar un valor y una cadena!")
print("==============================================================================")
dict = {"nombre": "Nahuel", "edad": 25}
try:
    telefono = dict["telefono"]
    print(f"el telefono es {telefono}")
except KeyError:
    # No se encuentra la clave en el diccionario
    print("No existe la clave telefono en el diccionario")
print("==============================================================================")    
try:
    archivo = open("archivo.txt")
except FileNotFoundError:
    # no existe el archivo que se quiere abrir
    print("No existe el archivo que quiere abrirse")    
print("==============================================================================")    
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
print("==============================================================================") 