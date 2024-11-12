def media_armonica(lista):
    soma = 0
    for c in lista:
        soma += c * 2
    print(soma)
    return len(lista) / soma
lista = [1, 2, 4]
print(media_armonica(lista))