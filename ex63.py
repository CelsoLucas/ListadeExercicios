def calcular_juros_compostos(capital, taxa, tempo, n = 1):
    valor_final = capital * (1 + taxa / n) ** (n * tempo)
    return valor_final


capital_inicial = 1000  
taxa_juros = 0.05       
tempo_anos = 3          

valor_final = calcular_juros_compostos(capital_inicial, taxa_juros, tempo_anos)
print(f"Valor final: R${valor_final:.2f}")  
