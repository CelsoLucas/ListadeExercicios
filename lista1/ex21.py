def media_lista(lista):
    soma = 0
    for i in lista:
        soma += i
    media = soma / len(lista)
    return media
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = media_lista(lista)
print(result)