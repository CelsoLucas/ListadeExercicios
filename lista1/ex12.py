def eh_palindromo(s):
    if s[::-1] == s:
        return "É palindromo"
    else:
        return "Não é palindromo"
s = str(input("Texto: "))
result = eh_palindromo(s)
print(result)