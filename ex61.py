def bubblesort(lista):
    cont1 = 0
    cont2 = 1
    saver = 0
    while lista != sorted(lista):
        if cont2 == len(lista):
            cont1 = 0
            cont2 = 1
        if lista[cont1] > lista[cont2]:
            saver = lista[cont1]
            lista[cont1] = lista[cont2]
            lista[cont2] = saver
        else:
            cont1 += 1
            cont2 += 1
    return lista
lista = [4, 8, 2, 1, 3, 5, 9, 6, 7, 10]
print(bubblesort(lista))