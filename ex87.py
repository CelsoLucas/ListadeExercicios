def gerar_numeros(n):
    cont = 0
    for c in range(n):
        if c % 2 == 0:
            print(c)
            cont += 1
    return c

# Exemplo de uso
n = 10
numeros = gerar_numeros(n)
print(f"Números de 1 até {n}: {numeros}")
