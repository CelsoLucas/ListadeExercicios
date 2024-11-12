import re

def validar_senha(senha):
    if len(senha) < 8:
        return "A senha deve ter pelo menos 8 caracteres."

    if not re.search(r"[A-Z]", senha):
        return "A senha deve conter pelo menos uma letra maiúscula."

    if not re.search(r"[a-z]", senha):
        return "A senha deve conter pelo menos uma letra minúscula."

    if not re.search(r"[0-9]", senha):
        return "A senha deve conter pelo menos um dígito."

    if not re.search(r"[!@#$%^&*()_+=\-{}\[\]:\";'<>?,./]", senha):
        return "A senha deve conter pelo menos um caractere especial."

    return "Senha válida."

senha = "Exemplo@123"
print(validar_senha(senha))

