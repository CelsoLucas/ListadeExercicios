def torre_hanoi(n, ori, des, aux):
    if len(n) <= 1:
        print(f"Mova o disco 1  de {ori} para {des}")
        return "TExto"
    # torre_hanoi(n[-1], ori, des, aux)
    if origem[-1] <= destino[-1]:
        destino.append(origem[-1])
        print(f"Mova o disco {origem[-1]} de {ori} para {des}")
        del origem[-1]
        del destino[0]
        return torre_hanoi(n, ori, des, aux)

    elif origem[-1] > destino[-1] and origem[-1] < auxiliar[-1]:
        auxiliar.append(origem[-1])
        print(f"Mova o disco {origem[-1]} de {ori} para {aux}")
        del auxiliar[0]
        del origem[-1]
        return torre_hanoi(n, ori, des, aux)

    
    if destino[-1] < auxiliar[-1]:
        auxiliar.append(destino[-1])
        print(f"Mova o disco {destino[-1]} de {des} para {aux}")
        return torre_hanoi(n, ori, des, aux)
    
    elif destino[-1] > auxiliar[-1] and destino[-1] < origem[-1]:
        origem.append(destino[-1])
        print(f"Mova o disco {destino[-1]} de {des} para {ori}")
        return torre_hanoi(n, ori, des, aux)

    


n = [5, 4, 3, 2, 1]
origem = [5, 4, 3, 2, 1]
destino = [1]
auxiliar = [5]
print(torre_hanoi(n, "A", "B", "C"))
print(origem)
print(destino)
print(auxiliar)
