def soma_lista(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = soma_lista(lista)
print(result)
