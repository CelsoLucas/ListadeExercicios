class Sort:
    def selection_sort(lista):
        for i in range(len(lista)):
            menor_index = i
            for j in range(i+1, len(lista)):
                if lista[j] < lista[menor_index]:
                    menor_index = j
                
            lista[i], lista[menor_index] = lista[menor_index], lista[i]

        return lista

