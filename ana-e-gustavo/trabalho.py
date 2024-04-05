import time
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Definindo função para abrir um artigo (.txt) diferente.
def ler_nome_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None
    
# Definindo função para gerar nuvem de palavras
# Usando como base o site "https://amueller.github.io/word_cloud/auto_examples/simple.html#sphx-glr-auto-examples-simple-py"    
def gerando_word_cloud(conteudo):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(conteudo)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

# Função Principal do Código
def main():
     # Solicitação ao usuário do nome do arquivo
    nome_arquivo = input("Escreva o nome do arquivo .txt: ")
    # Abrir o arquivo
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return        

    # Loop para a escolha das opções do usuário dentro do Menu Interativo
    while True:
        # Menu Interativo
        print("\nMenu Interativo")
        print("1. Número de palavras")
        print("2. Número de palavras distintas")
        print("3. Número de linhas")
        print("4. Frequência das palavras")
        print("5. Imprimir uma linha específica")
        print("6. Buscar uma palavra e imprimir a linha em que aparece a primeira ocorrência")
        print("7. Substituir todas as ocorrências de uma palavra por outra")
        print("8. Abrir um outro livro")
        print("9. Encerrar o programa")
        print("10. Gerar nuvem de palavras")

        # Pergunta ao usuário a opção desejada
        opcao = int(input("\nEscolha a opção: "))

        # Opções para escolha

        # 1. Número de palavras
        if opcao == 1:
            palavras = conteudo.split()
            print("O número de palavras é:", len(palavras))
            time.sleep(2)

        # 2. Número de palavras distintas
        elif opcao == 2:
            palavras_distintas = set(conteudo.split())
            print("O número de palavras distintas é:", len(palavras_distintas))
            time.sleep(2)

        # 3. Número de linhas
        elif opcao == 3:
            linhas = conteudo.splitlines()
            print("O número de linhas é:", len(linhas))
            time.sleep(2)

        # 4. Frequencia das palavras
        elif opcao == 4:
            palavras = conteudo.lower().split()
            frequencia = {}
            for palavra in palavras:
                frequencia[palavra] = frequencia.get(palavra, 0) + 1
            for palavra, contar in frequencia.items():
                print(f"A palavra '{palavra}'aparece {contar} vezes")
            time.sleep(2)

        # 5. Imprimir uma linha específica
        elif opcao == 5:
            numero_linha = int(input("Digite a linha que você deseja imprimir: "))
            linhas = conteudo.split('\n')
            if 1 <= numero_linha <= len(linhas):
                print(linhas[numero_linha - 1])
            else:
                print("Linha não encontrada")
            time.sleep(2)

        # 6. Buscar uma palavra e imprimir a linha em que aparece a primeira ocorrência da palavra
        elif opcao == 6:
            consulta = input("Insira a palavra que deseja buscar: ").lower()
            encontrou = False
            for index, linha in enumerate(conteudo.split('\n'), start=1):
                if consulta in linha.lower():
                    print(f'A primeira ocorrência é na linha {index}: {linha.strip()}')
                    encontrou = True
                    break
            if not encontrou:
                print("Palavra não encontrada")
            time.sleep(2)


#ARRUMAR
        # 7. Substituir todas as ocorrências de uma palavra por outra --> Só está substituindo uma ocorrência
        elif opcao == 7:
            palavra_anterior = input("Digite a palavra que você deseja substituir: ")
            palavra_nova = input("Digite a nova palavra: ")
            conteudo = conteudo.replace(palavra_anterior, palavra_nova)
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                arquivo.write(conteudo)
            print("O artigo foi atualizado e as palavras foram alteradas.")
            time.sleep(2)

        # 8. Abrir um outro artigo
        elif opcao == 8:
            nome_arquivo = input("Digite o nome do novo arquivo .txt: ")
            novo_conteudo = ler_nome_arquivo(nome_arquivo)
            if novo_conteudo is not None:
                conteudo = novo_conteudo
                print("Novo arquivo carregado com sucesso.")
            else:
                print("Voltando ao menu principal.")
            time.sleep(2)

        # 10. Gerar nuvem de palavras
        elif opcao == 10:
            gerando_word_cloud(conteudo)
            time.sleep(2)

        # 9. Fecha o Arquivo
        elif opcao == 9:
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")

main()