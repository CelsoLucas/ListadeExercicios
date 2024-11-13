class Contador():
    def cont(s):
        cont = 0
        lista_vogais = ["A", "E", "I", "O", "U", " "]
        for l in s:
            if l not in lista_vogais:
                cont += 1
        return cont