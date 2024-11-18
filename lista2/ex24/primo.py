def numeros_primos(n):
    lista2 = []
    if n > 1:
        for c in range(2, n+1):
            for i in range(2, n+1):
                if i % c == 0:
                    lista2.append(c)
        return lista2
