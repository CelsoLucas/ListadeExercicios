def maior_elemnto(lista):
    maior = lista[0]
    for c in lista:
        if c >= maior:
            maior = c
    return maior
lista = [1, 2, 3, 4, 6, 8, 9, 0, 100]
result = maior_elemnto(lista)
print(result)
