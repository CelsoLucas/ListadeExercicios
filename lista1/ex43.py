def multiplicar(a, b):
    if b == 0:
        return 0
    return a + multiplicar(a, b - 1)
print(multiplicar(3, 4))