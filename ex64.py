import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ""
    for c in range(tamanho):
        senha += random.choice(caracteres)
    return senha

tamanho_senha = 12
senha_gerada = gerar_senha(tamanho_senha)
print(f"Senha gerada: {senha_gerada}")
