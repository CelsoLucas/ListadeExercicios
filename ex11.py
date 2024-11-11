def conta_palavras(texto):
    palavras = texto.split()
    return len(palavras)
texto = str(input("Texto: "))
print(conta_palavras(texto))