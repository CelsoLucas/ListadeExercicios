def contar_elementos(lista):
    contagem = {}
    for elemento in lista:
        if elemento in contagem:
            contagem[elemento] += 1
        else:
            contagem[elemento] = 1
    return contagem

lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
resultado = contar_elementos(lista)
print(resultado)
