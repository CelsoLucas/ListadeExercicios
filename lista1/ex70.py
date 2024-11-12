def classificar_triangulo(a, b, c):

    if a + b <= c or a + c <= b or b + c <= a:
        return "Não é um triângulo válido."

    if a == b == c:
        return "Triângulo Equilátero"
    elif a == b or a == c or b == c:
        return "Triângulo Isósceles"
    else:
        return "Triângulo Escaleno"

a = 5
b = 5
c = 5
tipo = classificar_triangulo(a, b, c)
print(f"O triângulo com lados {a}, {b}, {c} é: {tipo}")
