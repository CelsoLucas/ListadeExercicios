def conta_letras(s, letras):
    cont = 0
    contador = 0
    for c in s:
        if letras == s[contador]:
            cont += 1
        contador += 1
    return cont
s = str(input("Digite um texto: "))
letras = str(input("Digite uma letra: "))
result = conta_letras(s, letras)
print(result)