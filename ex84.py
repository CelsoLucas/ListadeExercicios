def converter_12h_para_24h(hora_12h):
    periodo = hora_12h[-2:].upper() 
    hora = int(hora_12h[:2])
    minutos = hora_12h[3:5]

    if periodo == "AM":
        if hora == 12:  
            hora = 0
    elif periodo == "PM":
        if hora != 12: 
            hora += 12

    return f"{hora:02}:{minutos}"

hora_12h = "02:30 PM"
hora_24h = converter_12h_para_24h(hora_12h)
print(f"A hora {hora_12h} no formato 24 horas é: {hora_24h}")
