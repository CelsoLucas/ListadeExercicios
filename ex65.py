def dec2bin(numero):
    if numero == 0:
        return "0"
    
    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2
    
    return binario

# Exemplo de uso
numero_decimal = 10
binario = dec2bin(numero_decimal)
print(f"Decimal: {numero_decimal} -> Binário: {binario}")
