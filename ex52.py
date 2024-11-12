def soma_diagonais(matriz):
    n = len(matriz)
    soma_principal = 0
    for i in range(n):
            soma_principal += matriz[i][2-i]
    return soma_principal * 2
matriz = [[5, 2, 8],
          [4, 5, 6],
          [3, 8, 4]
        ]
print(soma_diagonais(matriz))