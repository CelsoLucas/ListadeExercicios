def troca_vogais(s, letra):
    vogais = "aeiouAEIOU"
    resultado = ""
    for char in s:
        if char in vogais:
            resultado += letra
        else:
            resultado += char
    return resultado

s = str(input("Texo: "))
letra = str(input("Letra: "))
result = troca_vogais(s, letra)
print(result)