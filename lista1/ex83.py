def adicionar_dias_a_data(data, n):
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
    
    def converter_dias_em_data(dias):
        dias_no_ano = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ano = 1
        while dias > 365:
            if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
                dias -= 366
            else:
                dias -= 365
            ano += 1
        mes = 1
        while dias > dias_no_ano[mes - 1]:
            dias -= dias_no_ano[mes - 1]
            mes += 1
        dia = dias
        return f"{dia:02}/{mes:02}/{ano}"

    ano, mes, dia = converter_data(data)
    dias_iniciais = dias_desde_ano_0(ano, mes, dia)

    nova_data_em_dias = dias_iniciais + n

    nova_data = converter_dias_em_data(nova_data_em_dias)

    return nova_data

data = "11/11/2024"
dias_para_adicionar = 10
nova_data = adicionar_dias_a_data(data, dias_para_adicionar)
print(f"A nova data após adicionar {dias_para_adicionar} dias é: {nova_data}")
