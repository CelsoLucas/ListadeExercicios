def conta_maiusculas(texto):
    cont = 0
    for c in texto:
        if c.isupper():
            cont += 1
    return cont
print(conta_maiusculas("Celso Lucas dos Santos Primon"))