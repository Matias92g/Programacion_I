"""
Crear una función recursiva en Python que reciba un número entero positivo en base 
decimal y devuelva su representación en binario como una cadena de texto.
Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y 
unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este procedimiento:
1. Dividir el número por 2.
2. Guardar el resto (0 o 1).
3. Repetir el proceso con el cociente hasta que llegue a 0.
4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
Convertir el número 10 a binario:
10 ÷ 2 = 5 resto: 0 
5 ÷ 2 = 2 resto: 1 
2 ÷ 2 = 1 resto: 0 
1 ÷ 2 = 0 resto: 1 
Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".
"""


def convertir_a_binario(numero):
    if numero == 0:
        return "0"
    elif numero == 1 :
        return "1"
    else:
        return convertir_a_binario(numero//2) + str(numero % 2)

print(convertir_a_binario(10))