"""
    dados dos conjuntos A y B
    1. imprimir los elementos que esten en A o B o en ambos
    2. Que se encuentren en A y en B
    3. En A o en B pero no ambos
    4. Dado un A imprimir si el conjunto es subconjunto de B
    5. Dado un A imprimir el numero de elementos en el conjunto
"""

#1
A = {1,2,3,4,5,6,7,8}
B = {1,2,4,5,7,8,9}

def imprimir_todo():
    print(A.union(B))
    
imprimir_todo()
#2
def imprimir_ambos():
    print(A & B)
imprimir_ambos()

#3
def imprimir_AoB_peroNoAmbos():
    print(A.symmetric_difference(B))

imprimir_AoB_peroNoAmbos()
#4.

def imprimir_subconjunto():
    print(A.issubset(B))

imprimir_subconjunto()    

#5
def contarA():
    print(len(A))
contarA()