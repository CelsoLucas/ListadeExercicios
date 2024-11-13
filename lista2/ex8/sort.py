class Sort:
    def insertion_sort(lista):
        save = 0
        for i in range(1, len(lista)):
            chave = lista[i]
            while True:
                if lista[i - 1] > chave:
                    save = chave
                    lista[i] = lista[i - 1]
                    lista[i - 1] = save
                else:
                    break
        return lista