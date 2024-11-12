def maior(a, b):
    if a > b:
        return f"{a} é maior"
    elif b > a:
        return f"{b} é maior"
    else:
        return "Os números são iguais"
a = float(input("n1: "))
b = float(input("n2: "))
n = maior(a, b)
print(n)

def maior(a, b):
    if a > b:
        print(f"{a} é maior")
    elif b > a:
        print(f"{b} é maior")
    else:
        print("Os números são iguais")
a = float(input("n1: "))
b = float(input("n2: "))
maior(a, b)