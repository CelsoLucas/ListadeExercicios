import soma
import subtracao
import multiplicacao
import divisao

class Calculadora:
    def calcular(opcao, n1, n2):
        if opcao == 1:
            resultado = soma.Soma.somar(n1, n2)
            print(f"{n1} + {n2} = {resultado}")
        elif opcao == 2:
            resultado = subtracao.Subtracao.subtrair(n1, n2)
            print(f"{n1} - {n2} = {resultado}")
        elif opcao == 3:
            resultado = multiplicacao.Multiplicacao.multiplicar(n1, n2)
            print(f"{n1} X {n2} = {resultado}")
        elif opcao == 4:
            resultado = divisao.Divisao.dividir(n1, n2)
            print(f"{n1} / {n2} = {resultado}")
        else:
            print("Opção Invalida!")
        
        return resultado