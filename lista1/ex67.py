def valida_email(email):
    gmail = ["@gmail.com", "@outlook.com", "@hotmail.com", "@icloud.com"]
    arroba = email.index("@")
    emailpt1 = email[:arroba]
    emailpt2 = email[arroba:]
    if emailpt2 in gmail:
        return "Email valido"
    else:
        return "Email invalido"

print(valida_email("lucascelso23@gkil.com"))