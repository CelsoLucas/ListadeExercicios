def filtra_pares(lista):
    par = []
    for c in lista:
        if c % 2 == 0:
            par.append(c)
    return par
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filtra_pares(lista))