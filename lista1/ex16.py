def retira_espacos(texto):
    inteiro = ""
    sem_espaco = texto.split()
    for t in sem_espaco:
        inteiro += t
    return inteiro
texto = str(input("Texto: "))
result = retira_espacos(texto)
print(result)