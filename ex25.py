def remove_duplicados(lista):
    return list(set(lista))
lista = ["Celso", "Celso", "Anne", "Ederson"]
result = remove_duplicados(lista)
print(result)