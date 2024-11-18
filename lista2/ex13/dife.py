def diferenca_consecutiva(lista):
    soma = 0
    listas = []
    for c in range(len(lista)-1):
        soma = abs(lista[c] - lista[c+1])
        listas.append(soma)
    return listas
