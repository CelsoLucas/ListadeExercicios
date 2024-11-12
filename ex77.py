def ler_conteudo_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        return f"O arquivo '{nome_arquivo}' não foi encontrado."
    except Exception as e:
        return f"Erro ao ler o arquivo: {e}"

nome_arquivo = "exemplo.txt"
conteudo = ler_conteudo_arquivo(nome_arquivo)
print(conteudo)
