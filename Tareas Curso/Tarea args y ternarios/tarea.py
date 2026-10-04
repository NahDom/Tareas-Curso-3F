#1 calcular el mayor de dos números ingresados por teclado usando un operador ternario

a = int(input("ingrese el primer valor: "))
b = int(input("ingrese el segundo valor: "))
mayor = a if a > b else b
print(f"el mayor valor es {mayor}")

#2.buscar una palabra en una lista ingresada por teclado usando args y un operador ternario

def busqueda(palabra,*args):
    return "existe en la lista" if palabra in args else "no existe en la lista la palabra buscada"

lista_ingresada = input("Ingrese la palabra separada por espacios: ").split()
# elementos que se almacenan en la lista de argumentos ingresados
# split me lo separa en elementos separados ya para no pedir constantemente al usuario
palabra_buscar = input("Ingrese la palabra que quiere buscar: ")
# elementos ingresados en la lista de palabras

print(busqueda(palabra_buscar, *lista_ingresada))
print(lista_ingresada)

#3. determinar si un numero es par o impar

numero = int(input("Ingrese un numero: "))
es_par = "Numero par" if numero % 2 == 0 else "Numero Impar"
print(es_par)

#4. calcular el promedio de una lista de números usando args y un operador ternario

# como el promedio es la suma de los valores dividido la cantidad de elementos puedo hacer la suma de elementos de los argumentos ingresados dividida el tamaño total de elementos en la lista
def promedio(*args):
    return sum(args) / len(args) if args else 0

print("el valor promedio de elementos en la lista es: ",promedio(10, 8, 9, 20, 50, 100)) 

#5. imprimir un mensaje de error si no se pasan suficientes argumentos

def verificador_cantidad(*args):
    minimo_requerido = 5
    return "Exito" if len(args) >= minimo_requerido else "Error, faltan argumentos"
print(verificador_cantidad(1, 2, 3, 4))