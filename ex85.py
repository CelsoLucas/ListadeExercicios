def converter_24h_para_12h(hora_24h):
    hora, minutos = map(int, hora_24h.split(':'))

    if hora == 0:
        hora_12h = 12
        periodo = "AM"
    elif hora < 12:
        hora_12h = hora
        periodo = "AM"
    elif hora == 12:
        hora_12h = 12
        periodo = "PM"
    else:
        hora_12h = hora - 12
        periodo = "PM"

    return f"{hora_12h:02}:{minutos:02} {periodo}"

hora_24h = "14:30"
hora_12h = converter_24h_para_12h(hora_24h)
print(f"A hora {hora_24h} no formato 12 horas é: {hora_12h}")
