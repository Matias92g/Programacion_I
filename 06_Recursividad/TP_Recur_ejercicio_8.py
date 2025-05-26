"""
Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
aparece ese dígito dentro del número.
 Ejemplos:
contar_digito(12233421, 2) → 3 
contar_digito(5555, 5) → 4 

"""
def contar_digitos(numero, digito):
    if numero == 0:
        return 0
    else:
        return (1 if digito == numero % 10 else 0) + contar_digitos(numero // 10, digito)
 
print(contar_digitos(12233421,2))
print(contar_digitos(5555,5))
print(contar_digitos(123456, 7))

