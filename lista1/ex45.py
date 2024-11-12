def somatoria_lista_recursivo(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + somatoria_lista_recursivo(lista[1:])
print(somatoria_lista_recursivo([1, 2, 3, 4]))
