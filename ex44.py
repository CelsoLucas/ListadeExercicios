def potencia_recursiva(base, exp):
    if exp == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exp - 1)
print(potencia_recursiva(5, 4))