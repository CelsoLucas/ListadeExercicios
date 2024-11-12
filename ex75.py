def inverter_chaves_valores(dicionario):
    return {valor: chave for chave, valor in dicionario.items()}

dicionario = {'a': 10, 'b': 20, 'c': 30}
resultado = inverter_chaves_valores(dicionario)
print(resultado)
