def eh_par(num):
    if num % 2 == 0:
        return "True"
    else:
        return "False"
num = int(input("Digite um número: "))
n = eh_par(num)
print(n)

def eh_par(num):
    if num % 2 == 0:
        print("True")
    else:
        print("False")
num = int(input("Digite um número: "))
eh_par(num)