def mult_pares(lista):
    p = 1
    result = 0
    for c in lista:
        if c % 2 == 0:
            result = c * p
            p = result
    return result