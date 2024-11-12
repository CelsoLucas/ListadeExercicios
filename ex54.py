def media_notas(dicionario):
    tamanho = len(dicionario)
    soma = 0
    for c in dicionario:
        soma += dicionario[c]
    return soma / tamanho
dicionario = {"Celso":10, "Anne":6, "Ederson":9}
print(media_notas(dicionario))
