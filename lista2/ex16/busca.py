def busca_binaria(lista, ele):
    for c in range(0, len(lista)+1):
        if lista[c] == ele:
            return c
    return -1
    