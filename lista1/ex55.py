def converte_segundos(h, m, s):
    hr_m = h * 60
    m_s = m * 60
    return f"{h} horas é {hr_m} em minutos\n{m} minutos é {m_s} em segundos"
print(converte_segundos(2, 180, 1000))