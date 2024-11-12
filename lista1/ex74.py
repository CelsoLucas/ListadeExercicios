def ordena_por_valores(dicionario, reverso=False):
    return dict(sorted(dicionario.items(), key=lambda item: item[1], reverse=reverso))

dicionario = {'a': 10, 'b': 20, 'c': 5, 'd': 30}

resultado_crescente = ordena_por_valores(dicionario)
print("Ordenado de forma crescente:", resultado_crescente)

resultado_decrescente = ordena_por_valores(dicionario, reverso=True)
print("Ordenado de forma decrescente:", resultado_decrescente)
