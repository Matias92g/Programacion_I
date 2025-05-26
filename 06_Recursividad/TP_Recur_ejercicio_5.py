import unicodedata

#Función para eliminar los tildes
def eliminar_tildes(texto):
    return unicodedata.normalize("NFD", texto).encode("ascii", "ignore").decode("utf-8")

def es_palindromo(palabra):
    
    palabra_sin_espacios = "".join(palabra.split()) #elimina los espacios estre palabras
    palabra_sin_tilde = eliminar_tildes(palabra_sin_espacios) #devulve la palabra ingresada sin tildes.
    palabra_limpia = palabra_sin_tilde.lower() #convierte todo el texto a minusculas.

    if len(palabra_limpia) <= 1:
        return True
    # Comparar extremos y hacer llamada recursiva con el texto reducido
    if palabra_limpia[0] != palabra_limpia[-1]:
        return False
    return es_palindromo(palabra_limpia[1:-1])

print(es_palindromo("Ana ná"))
print(es_palindromo("Neuquén"))
print(es_palindromo("Programación I"))


