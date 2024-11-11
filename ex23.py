def menor_elemnto(lista):
    menor = lista[0]
    for c in lista:
        if c <= menor:
            menor = c
    return menor
lista = [1, 2, 3, 4, 6, 8, 9, 0, 100]
result = menor_elemnto(lista)
print(result)
