def division_entre_dos_numeros(x,y):
    try:
        dividendo = x
        divisor = y 
        return dividendo / divisor
    except ZeroDivisionError:
        return "No puede dividirse por cero, intente con otro"
    
def main():
    x = input(int("Ingrese el primer valor: "))
    y = input(int("Ingrese el segundo valor: "))
    print(division_entre_dos_numeros(x,y))