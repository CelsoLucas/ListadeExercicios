def fatorial(n):
    resultado = 1
    cont = 1
    while cont <= n:
        resultado *= cont
        cont += 1
    print(resultado)
n = 5
fatorial(n)