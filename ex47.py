def conta_ocorrencias_recursiva(lista, ele):
    if not lista:
        return 0
    if lista[0] == ele:
        return 1 + conta_ocorrencias_recursiva(lista[1:], ele)
    else:
        return conta_ocorrencias_recursiva(lista[1:], ele)
lista = [1, 2, 3, 5, 2, 2, 1, 1, 1]
print(conta_ocorrencias_recursiva(lista, 1))