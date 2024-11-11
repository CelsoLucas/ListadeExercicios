def ocorrencias_palavras(texto):
    texto = texto.lower()
    palavras = texto.split()
    contagem = {}

    for palavra in palavras:
        palavra = ''.join(char for char in palavra if char.isalnum())
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    return contagem
texto = str(input("Texto: "))
result = ocorrencias_palavras(texto)
print(result)