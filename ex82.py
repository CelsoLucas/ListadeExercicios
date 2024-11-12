def dias_entre_datas(data1, data2):
    def converter_data(data):
        dia, mes, ano = map(int, data.split('/'))
        return ano, mes, dia
    
    def dias_desde_ano_0(ano, mes, dia):
        dias_no_ano = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        dias = (ano - 1) * 365 + sum([1 for i in range(1, ano) if (i % 4 == 0 and (i % 100 != 0 or i % 400 == 0))])
        dias += sum(dias_no_ano[:mes-1])
        if mes > 2 and (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
            dias += 1
        dias += dia
        return dias

    ano1, mes1, dia1 = converter_data(data1)
    ano2, mes2, dia2 = converter_data(data2)
    
    return abs(dias_desde_ano_0(ano1, mes1, dia1) - dias_desde_ano_0(ano2, mes2, dia2))

data1 = "11/11/2024"
data2 = "01/01/2020"
diferenca = dias_entre_datas(data1, data2)
print(f"A diferença entre as datas é de {diferenca} dias.")
