def conta_ocorrencia(lista, elemento):
    cont = 0
    for c in lista:
        if c == elemento:
            cont += 1
    return cont
lista = ["Celso", "Anne", "Ederson", "Celso", "Celso"]
elemento = str(input("Elemento: "))
result = conta_ocorrencia(lista, elemento)
print(result)