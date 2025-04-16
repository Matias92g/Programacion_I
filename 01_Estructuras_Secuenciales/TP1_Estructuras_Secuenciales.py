# 1)Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
# Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) 
# para realizar la impresión por pantalla.
nombre = input("Por favor ingresa tu nombre: ")
print (f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. 
# Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”.
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
nombre = input("Por favor ingresa tu nombre: ")
apellido = input("Por favor ingresa tu apellido: ")
edad = int(input(f"{nombre}, cuántos años tienes? "))
residencia= input (f"{nombre}, dónde vives actualmente? ")
print(f"Soy {nombre} {apellido}, tengo {edad} años de edad y vivo en {residencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
radio= int(input("Ingresa el radio de un círculo para calcular el área del mismo:  "))
pi= 3.141592
area= float(pi)* radio**2
print(area)

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos= int(input("Ingresa la cantidad de segundo que quieres expresar en horas: "))
horas = float(segundos)/3600
print(f"{segundos} equivalen a {horas} horas")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
num = int(input("Por favor ingresa un número entero:"))
print (f"Tabla de multiplicar de {num} del 1 al 10:")
print (f"1x{num}:",int((1*num)))
print (f"2x{num}:",int((2*num))) 
print (f"3x{num}:",int((3*num))) 
print (f"4x{num}:",int((4*num))) 
print (f"5x{num}:",int((5*num))) 
print (f"6x{num}:",int((6*num))) 
print (f"7x{num}:",int((7*num))) 
print (f"8x{num}:",int((8*num))) 
print (f"9x{num}:",int((9*num))) 
print (f"10x{num}:",int((10*num))) 

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1= int(input("ingresa un numero destinto de cero: "))
num2= int(input("ingresa un numero destinto de cero "))
if num1 != 0 and num2 !=0 :
    print(num2 + num1)
    print(num1/num2)
    print(num1*num2)
    print(num1-num2)
else: 
    print("Al menos uno de los números ingresados no es válido")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
# Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔/(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2
altura= float(input("ingresa tu altura en metros: "))
peso= float(input("ingresa tu peso en Kgs "))
imc = peso / (altura**2)
print(imc)

# 9) Crear un programa que pida al usuario una temperatura en grados 
# Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 =9/5.𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
temp1 = float(input("Indica cúal es la temperatura actual en °C : "))
temp2 = float((temp1 * (9/5)+32))
print(f"{temp1}°C equivalen a {temp2}°F")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
num1= int(input("ingresa un numero "))
num2= int(input("ingresa un numero "))
num3= int(input("ingresa un numero "))
promedio = (num1+num2+num3)/3
print(promedio)