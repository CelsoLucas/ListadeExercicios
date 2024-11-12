def gerar_quadrados(n):
    return [i**2 for i in range(1, n+1)]

n = 10
quadrados = gerar_quadrados(n)
print(f"Quadrados dos números de 1 até {n}: {quadrados}")
