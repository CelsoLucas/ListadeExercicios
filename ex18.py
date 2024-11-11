def alterna_maiusculas(texto):
    resultado = ""
    for l in texto:
        if l.isupper():
            resultado += l.lower()
        elif l.islower():
            resultado += l.upper()
        else:
            resultado += l
    return resultado
texto = str(input("Texto: "))
result = alterna_maiusculas(texto)
print(result)