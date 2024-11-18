def media_ponde(l_n, l_p):
    cima = 0
    for c in range(len(l_n)):
        cima += l_n[c] * l_p[c]
    soma = sum(l_p)
    mp = cima / soma
    return mp
