def mediana(lista):
    lista.sort()
    n = len(lista)
    if n % 2 != 0:
        return lista[n // 2]
    else:
        meio1 = lista[n // 2 - 1]
        meio2 = lista[n // 2]
        return (meio1 + meio2) / 2
lista = [1, 6, 2, 9, 3, 8, 9, 2]
print(mediana(lista))
