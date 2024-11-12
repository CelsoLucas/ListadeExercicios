def merge_dicionarios(d1, d2):
    resultado = d1.copy()

    for chave, valor in d2.items():
        if chave in resultado:
            resultado[chave] += valor
        else:
            resultado[chave] = valor

    return resultado

# Exemplo de uso
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 5, 'c': 15, 'd': 25}

resultado = merge_dicionarios(d1, d2)
print(resultado)
