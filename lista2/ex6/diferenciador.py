class Diferenca:
    def diferenca_conjustos(lista1, lista2):
        lista = []
        for c in lista1:
            if c not in lista2:
                lista.append(c)
        return lista