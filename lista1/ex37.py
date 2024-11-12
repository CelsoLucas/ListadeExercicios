def eh_armstrong(n):
    soma = 0
    for c in str(n):
        mult = int(c) ** 3
        soma += mult
    if soma == n:
        return True
    else:
        return False
print(eh_armstrong(371))