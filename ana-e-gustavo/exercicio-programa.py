# solicitação ao usuário do nome do arquivo
arquivo=str(input("Escreva o nome do arquivo .txt: "))
#ARRUMAR: entender o porquê ele não encontra o arquivo e como fazer para pegar o nome recebido e abrir
def abrir_arquivo(arquivo):
    try:
        with open(arquivo, "r+") as arquivo1:
            return arquivo1.read()
    except FileNotFoundError:
        print("Erro aquivo: {arquivo1}")
opcao = 0


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
    opcao=int(input("\n Escolha a opção: "))
    texto = abrir_arquivo(arquivo)

    #opções para escolha
    if opcao == 1:
        #1. Número de palavras
        #ARRUMAR: len() conta o número de caracteres, e não palavras
        tamanho = len(texto)
        print("O número de palavras é: ", tamanho)

    else:
        print("Opção inválida.")