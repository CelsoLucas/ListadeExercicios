def multiplica_matriz(lista1, lista2):
    lista3 = []
    for i in range(2):
        for j in range(2):
            novo = lista1[i][j] * lista2[i][j]
            lista3.append(novo)
    return lista3