def conta_vogais(texto):
    cont = 0
    for l in range(len(texto)):
        if texto[l] == "a" or texto[l] == "e" or texto[l] == "i" or texto[l] == "o" or texto[l] == "u":
            cont += 1
    return cont
texto = str(input("Digite um texto: "))
total = conta_vogais(texto)
print(total)

def conta_vogais(texto):
    cont = 0
    for l in range(len(texto)):
        if texto[l] == "a" or texto[l] == "e" or texto[l] == "i" or texto[l] == "o" or texto[l] == "u":
            cont += 1
    print(cont)
texto = str(input("Digite um texto: "))
conta_vogais(texto)
