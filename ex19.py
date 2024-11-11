def apaga_vogais(s):
    vogais = "aeiouAEIOU"
    resultado = ""
    for l in s:
        if l not in vogais:
            resultado += l
    return resultado
s = str(input("Texo: "))
result = apaga_vogais(s)
print(result)