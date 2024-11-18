def merge_sort(lista):
    meio = len(lista) // 2

    esquerda = lista[:meio]
    direita = lista[meio:]
    
    if len(esquerda) > 1:
        esquerda = merge_sort(esquerda)
    if len(direita) > 1:
        direita = merge_sort(direita)

print(merge_sort([1, 2, 3, 4, 5, 6]))
def merge(esquerda, direita):
    pass