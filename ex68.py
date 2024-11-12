import os

def tamanho_arquivo(caminho):

    try:
        tamanho = os.path.getsize(caminho)
        return tamanho
    except FileNotFoundError:
        return f"O arquivo no caminho '{caminho}' não foi encontrado."

caminho_arquivo = "ex67.py"
tamanho = tamanho_arquivo(caminho_arquivo)
print(f"Tamanho do arquivo: {tamanho} bytes")
