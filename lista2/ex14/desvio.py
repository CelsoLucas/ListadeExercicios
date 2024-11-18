from math import sqrt
def desvio_padrao(lista):
    soma = 0
    media = sum(lista) / len(lista)
    for c in lista:
        soma += (c - media) ** 2
    desvio = sqrt((soma/len(lista)))
    return desvio