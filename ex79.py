def contar_palavras_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            palavras = conteudo.split()
            return len(palavras)
    except FileNotFoundError:
        return f"O arquivo '{nome_arquivo}' não foi encontrado."
    except Exception as e:
        return f"Erro ao ler o arquivo: {e}"

nome_arquivo = "exemplo.txt"
numero_palavras = contar_palavras_arquivo(nome_arquivo)
print(f"O número total de palavras no arquivo é: {numero_palavras}")
