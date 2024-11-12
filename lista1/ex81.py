def formatar_data(data_pura):
    dia = data_pura[:2]
    mes = data_pura[2:4]
    ano = data_pura[4:]
    return f"{dia}/{mes}/{ano}"
data_pura = "13102007"
data_formatada = formatar_data(data_pura)
print(f"Data formatada: {data_formatada}")
