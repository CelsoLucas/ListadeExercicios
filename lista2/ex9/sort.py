def quick_sort_iterativo(lista):
    # Pilha para armazenar os intervalos
    pilha = []
    
    # Empilha o intervalo completo da lista
    pilha.append((0, len(lista) - 1))
    
    # Processa os intervalos enquanto a pilha não estiver vazia
    while pilha:
        # Retira um intervalo da pilha
        inicio, fim = pilha.pop()
        
        # Particiona a lista e encontra o índice do pivô
        if inicio < fim:
            pivo_idx = particionar(lista, inicio, fim)
            
            # Empilha os subintervalos à esquerda e à direita do pivô
            pilha.append((inicio, pivo_idx - 1))  # Intervalo à esquerda do pivô
            pilha.append((pivo_idx + 1, fim))     # Intervalo à direita do pivô
    
    return lista

def particionar(lista, inicio, fim):
    # Escolhe o último elemento como pivô
    pivo = lista[fim]
    i = inicio - 1
    
    # Organiza a lista de forma que os menores elementos fiquem à esquerda
    # e os maiores fiquem à direita do pivô
    for j in range(inicio, fim):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    
    # Coloca o pivô na posição correta
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    
    # Retorna o índice do pivô
    return i + 1

# Exemplo de uso

