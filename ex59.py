def ordena_lista(lista):
    cont1 = 0
    cont2 = 1
    saver = 0
    for c in lista:
        if lista[cont1] > lista[cont2]:
            saver = lista[1]
            lista[1] = lista[2]
            lista[2] = saver
            if cont2 == len(lista):
                cont1 = 0
                cont2 = 1
    return lista
lista = [1, 6, 2, 7, 9, 3, 5, 8]
print(ordena_lista(lista))