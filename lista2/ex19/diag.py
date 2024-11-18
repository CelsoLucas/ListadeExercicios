def diag(matriz):
    diagonal_principal = []
    diagonal_secundaria = []
    for i in range(len(matriz)):
        diagonal_principal.append(matriz[i][i])
    for i in range(len(matriz)):
        diagonal_secundaria.append(matriz[i][len(matriz) - i - 1])
    
    return diagonal_principal, diagonal_secundaria
