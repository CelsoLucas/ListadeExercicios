def produto_escalar(v1, v2):
    produto = 0
    for c in range(len(v1)):
        produto += v1[c] * v2[c]
    return produto