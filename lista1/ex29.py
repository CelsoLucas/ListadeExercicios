def intersencao_listas(lista1, lista2):
    return list(set(lista1) & set(lista2))
lista1 = [1, 2, 3]
lista2 = [2, 1, 6]
result = intersencao_listas(lista1, lista2)
print(result)