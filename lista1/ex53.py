def conta_ocorrencia_caracteres(s):
    lista = {}
    for caractere in s:
        if caractere in lista:
            lista[caractere] += 1
        else:
            lista[caractere] = 1
    return lista
print(conta_ocorrencia_caracteres("Celso lindo"))
