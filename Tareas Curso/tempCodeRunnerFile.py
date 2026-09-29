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