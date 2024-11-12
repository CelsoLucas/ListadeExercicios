def contar_linhas_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            return len(linhas)
    except FileNotFoundError:
        return f"O arquivo '{nome_arquivo}' não foi encontrado."
    except Exception as e:
        return f"Erro ao ler o arquivo: {e}"

nome_arquivo = "exemplo.txt"
numero_linhas = contar_linhas_arquivo(nome_arquivo)
print(f"O número de linhas no arquivo é: {numero_linhas}")
