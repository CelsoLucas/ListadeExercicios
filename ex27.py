def elementos_unicos(lista):
    resultado = []
    for c in lista:
        cont = lista.count(c)
        if cont == 1:
            resultado.append(c)
    return resultado
lista = [1, 2, 2, 3, 3, 4, 5, 6,6 ]
result = elementos_unicos(lista)
print(result)