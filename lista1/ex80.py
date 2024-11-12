def substituir_palavra_arquivo(nome_arquivo, palavra_antiga, palavra_nova):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
        
        conteudo_modificado = conteudo.replace(palavra_antiga, palavra_nova)
        
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(conteudo_modificado)
        
        print(f"As ocorrências de '{palavra_antiga}' foram substituídas por '{palavra_nova}' no arquivo '{nome_arquivo}'.")
    
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

nome_arquivo = "exemplo.txt"
palavra_antiga = "sol"
palavra_nova = "lua"
substituir_palavra_arquivo(nome_arquivo, palavra_antiga, palavra_nova)
