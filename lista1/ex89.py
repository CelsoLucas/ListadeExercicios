def fibonacci(n):
    sequencia = []
    a, b = 0, 1
    for _ in range(n):
        sequencia.append(a)
        a, b = b, a + b
    return sequencia

n = 10
sequencia_fibonacci = fibonacci(n)
print(f"Os primeiros {n} termos da sequência de Fibonacci: {sequencia_fibonacci}")
