def verifica_ano_bissexto(ano):
    if ano % 4 == 0:
        return "é bissexto"
    else:
        return "não é bissexto"
print(verifica_ano_bissexto(2088))