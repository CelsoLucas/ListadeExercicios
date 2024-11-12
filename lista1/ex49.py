def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a % b)

def mdc_lista(lista):
    if len(lista) == 1:
        return lista[0]
    return mcd(lista[0], mdc_lista(lista[1:]))
numeros = [48, 36]
print(mdc_lista(numeros)) 