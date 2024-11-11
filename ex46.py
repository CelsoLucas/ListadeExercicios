def inverte_string_recursiva(s):
    if not s:
        return ""
    a, *b = s[::-1]
    return a + inverte_string_recursiva(b[::-1])
print(inverte_string_recursiva("Celso Lindo"))  