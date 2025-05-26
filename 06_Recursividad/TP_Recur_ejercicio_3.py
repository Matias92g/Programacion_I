"""
Crea una función recursiva que calcule la potencia de un número base elevado a un 
exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1).
Prueba esta función en un algoritmo general."""

#Algoritmo general

def potencia_recursiva(base,potencia):
    if potencia == 0:
        return 1
    else:
        return base * potencia_recursiva(base,potencia-1)

base= int(input("ingresa un número de base para calcular potencia: "))
potencia= int(input("ingresa la potencia que deseas calcular del numero anterior: "))

print(potencia_recursiva(base, potencia))
