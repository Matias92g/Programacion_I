"""Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
especifique.
"""
pos = int(input("Ingrese la posición de la cual desea obtener el valor de fibonacci: "))
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos-1)+fibonacci(pos-2)
print(fibonacci(10))

for i in range (pos+1):
    print(fibonacci(i))