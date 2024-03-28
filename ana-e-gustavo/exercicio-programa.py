import codecs # Biblioteca de codificação de caracteres
import time

# Função Principal do Código
def main():
    # Solicitação ao usuário do nome do arquivo
    arquivo = str(input("Escreva o nome do arquivo .txt: "))
    # Abrir o arquivo
    try:
        arquivo = codecs.open(arquivo, "r+")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        exit()

    # Ler o conteúdo do arquivo
    conteudo = arquivo.read().encode("utf-8")
    opcao = 0 # Inicia sem função definida

    # Loop de escolha das opções do usuário dentro do Menu Interativo
    while opcao!=10:
        # Menu Interativo
        print("\n Menu Interativo")
        print("1. Número de palavras")
        print("2. Número de palavras distintas")
        print("3. Número de linhas")
        print("4. Frequência das palavras")
        print("5. Imprimir uma linha específica")
        print("6. Buscar uma palavra e imprimir a linha em que aparece a primeira ocorrência")
        print("7. Substituir todas as ocorrências de uma palavra por outra")
        print("8. Abrir um outro livro")
        print("9. Encerrar o programa")
        #print("10. Gerar nuvem de palavras")

        # Pedido ao usuário da opção desejada
        opcao = int(input("\nEscolha a opção: "))

        # Opções para escolha
        if opcao == 1:
            # 1. Número de palavras
            palavras = conteudo.split() # Manipulação da string como lista
            tamanho = len(palavras)
            print("O número de palavras é: ", tamanho)
            time.sleep(2)


        elif opcao == 9:
        # Encerrar o programa
            print("Programa encerrado.")
            exit()

        else:
            print("Opção inválida.")

    # Fecha o arquivo depois do uso        
    arquivo.close()
main()
