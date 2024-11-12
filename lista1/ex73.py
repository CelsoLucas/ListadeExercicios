def filtrar_dicionario(dicionario, valor):
    return {chave: val for chave, val in dicionario.items() if val > valor}

dicionario = {'a': 10, 'b': 20, 'c': 5, 'd': 30}
valor = 15

resultado = filtrar_dicionario(dicionario, valor)
print(resultado)
