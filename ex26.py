def soma_pares(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    return soma
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = soma_pares(lista)
print(result)