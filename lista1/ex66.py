def bin2dec(binario):
    decimal = 0
    for i, bit in enumerate(reversed(binario)):
        decimal += int(bit) * (2 ** i)
    return decimal


numero_binario = "1010"
decimal = bin2dec(numero_binario)
print(f"Binário: {numero_binario} -> Decimal: {decimal}")
