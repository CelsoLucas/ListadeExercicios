def criar_arquivo_com_texto(nome_arquivo, texto):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(texto)
    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")

nome_arquivo = "ex75.py"
texto = "Este é um exemplo de texto que será escrito no arquivo."

criar_arquivo_com_texto(nome_arquivo, texto)
