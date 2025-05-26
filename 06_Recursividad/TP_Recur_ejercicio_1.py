"""Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
función para calcular y mostrar en pantalla el factorial de todos los números enteros 
entre 1 y el número que indique el usuario"""

def factorial(numero):
    if numero == 0 :
        return 1
    else:
        return numero * factorial(numero-1)

def factoriales(num):
    for i in range (1, num+1):
        print(factorial(i))
print(factoriales(5))