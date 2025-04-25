#Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.

#Declaración de funciones a utilizar
def calcular_promedio(a,b,c):
    return (a+b+c)/3

#Programa Principal
a = int(input("Ingresa el 1er número: "))
b = int(input("Ingresa el 2do número: "))
c = int(input("Ingresa el 3er número: "))
print(f"El promedio de los números ingresados es: {calcular_promedio(a,b,c)}")