def eh_primo(n):
    if n <= 1:
        return "Não é primo"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return "Não é primo"
    return "É primo"
n = int(input("Número: "))
result = eh_primo(n)
print(result)