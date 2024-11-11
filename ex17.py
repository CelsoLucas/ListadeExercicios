def encontra_palavra(texto, palavra):
    return texto.count(palavra)
texto = str(input("Texto: ")).lower()
palavra = str(input("Palavra: ")).lower()
result = encontra_palavra(texto, palavra)
print(result)