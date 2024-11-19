import calculadora

while True:
    print("=-="*15)
    print("CALCULADORA DO CELSO")
    print("=-="*15)
    print("0 - Sair")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    while True:
        try:
            opcao = int(input("Digite a opção que deseja: "))
        except ValueError:
            print("Digite apenas números!")
            continue
        else:
            break
    
    while True:
        try:
            n1 = int(input("N1: "))
        except ValueError:
            print("Digite apenas números!")
        else:
            break
    while True:
        try:
            n2 = int(input("N2: "))
        except ValueError:
            print("Digite apenas números!")
        else:
            if opcao == 4 and n2 == 0:
                print(f"{n1} não pode ser dividido por zero!")
                continue
            break
    print("=-="*15)
    
    resultado = calculadora.Calculadora.calcular(opcao, n1, n2)
    