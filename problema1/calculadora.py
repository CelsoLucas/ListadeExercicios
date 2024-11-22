import soma
import subtracao
import multiplicacao
import divisao

class Calculadora():
    def __init__(self, opcao, n1, n2):
        self.opcao = opcao
        self.n1 = n1
        self.n2 = n2
        
    def calcular(self):
        if self.opcao == 1:
            operador = soma.Soma(self.n1, self.n2)
            resultado = operador.somar()
            print(f"{self.n1} + {self.n2} = {resultado}")
        elif self.opcao == 2:
            operador = subtracao.Subtracao(self.n1, self.n2)
            resultado = operador.subtrair()
            print(f"{self.n1} - {self.n2} = {resultado}")
        elif self.opcao == 3:
            operador = multiplicacao.Multiplicacao(self.n1, self.n2)
            resultado = operador.multiplicar()
            print(f"{self.n1} X {self.n2} = {resultado}")
        elif self.opcao == 4:
            operador = divisao.Divisao(self.n1, self.n2)
            resultado = operador.dividir()
            print(f"{self.n1} / {self.n2} = {resultado}")

        return resultado