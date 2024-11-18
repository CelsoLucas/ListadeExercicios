def separa_pares_impares(lista):
    lista_par = []
    lista_impar = []
    for c in lista:
        if c % 2 == 0:
            lista_par.append(c)
        else:
            lista_impar.append(c)
    return lista_par, lista_impar