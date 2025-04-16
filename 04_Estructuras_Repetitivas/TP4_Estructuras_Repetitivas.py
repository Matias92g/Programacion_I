# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for x in range(0,101):
    print(x)

print("-------------------------------------------------------------------------------------------------------")

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene.

num = str(input("Ingrese un nro entero: ")) #la función str() conbierte el entero ingresado por el usuario en string 
print(len(num)) #función len() determina la cantidad de caracteres.
print("-------------------------------------------------------------------------------------------------------")
# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores.

# Solicitar al usuario los dos valores
valor_inferior = int(input("Ingresa el primer valor (menor): "))
valor_superior = int(input("Ingresa el segundo valor (mayor): "))

# Verificar que los valores sean válidos
if valor_inferior >= valor_superior:
    print("El primer valor debe ser menor que el segundo. Por favor, inténtalo de nuevo.")
else:
    suma = 0  # Inicializar la suma
    # Recorrer los números entre los dos valores usando un bucle
    for numero in range(valor_inferior + 1, valor_superior):
        suma += numero
    
    # Mostrar el resultado de la suma
    print(f"La suma de los números entre {valor_inferior} y {valor_superior} es: {suma}")

print("-------------------------------------------------------------------------------------------------------")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

numero = int(input("Ingrese un numero: "))
suma= 0

while numero !=0:
    suma += numero
    numero = int(input("Ingrese otro numero: "))
print("La suma de los números ingresado es:", suma )
print("-------------------------------------------------------------------------------------------------------")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

#importación del módulo random
import random 

#Definición del rango
inicio_rango = 1
fin_rango = 10
#Almacenamiento de un número aleatorio en una variable
numero_aleatorio = random.randint(inicio_rango, fin_rango)

numero_seleccionado = int(input("Ingrese un número: "))
if numero_seleccionado == numero_aleatorio:
    print("Felicitaciones!, adivinaste el nro oculto!")
else:
    while numero_seleccionado != numero_aleatorio: 
        print("Estuvo cerca, pero no adivinaste el numero oculto!")
        numero_seleccionado = int(input("Ingrese otro número: "))
    print("Felicitaciones!, adivinaste el nro oculto!")

print("-------------------------------------------------------------------------------------------------------")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for x in range(100,0,-2):
    print(x)

print("-------------------------------------------------------------------------------------------------------")

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

#Solicitar al usuario el valor final del rango de numeros a sumar
fin_rango = int(input("Ingresa un número entero: "))
suma = 0
if fin_rango <0 :
    print("EL número ingresado debe ser positivo.")
else:
    for x in range (0, fin_rango):
        suma+=x
    # Mostrar el resultado de la suma
    print(f"La suma de los números entre 0 y {fin_rango} es: {suma}")

print("-------------------------------------------------------------------------------------------------------")
#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

#Inicialización de variables para el conteo de numeros pares e impares
contador_pares = 0
contador_impares= 0
#Usando el ciclo for definimos la cantidad de veces que se solicitará un nro al usuario.
for x in range(100):
    numero = int(input("Ingresa un número: "))
   #con la estructura condicional, verificacmos si el nro ingresado por el usuario es par o impar, y en función de esto, se modifica el contador correspondiente.
    if numero % 2 == 0 :
        contador_pares+=1
    else:
        contador_impares+=1
#Se imprime en pantalla la cantidad de nros pares e impares ingresados por el usuario.
print(f"De los numero ingresados, {contador_pares}, son pares")
print(f"De los numero ingresados, {contador_impares}, son impares")

print("-------------------------------------------------------------------------------------------------------")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor).

from statistics import median
suma = 0
for x in range(100):
    num = int(input("Ingrese otro número: "))
    suma += num
print(suma/100)

print("-------------------------------------------------------------------------------------------------------")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# Solicitar al usuario que ingrese un número
numero = input("Ingresa un número: ")

# Inicializar una variable para almacenar el número invertido
numero_invertido = ""

# Iterar a través de los dígitos del número, de derecha a izquierda
for digito in numero:
    numero_invertido = digito + numero_invertido

# Mostrar el resultado
print(f"El número invertido es: {numero_invertido}")