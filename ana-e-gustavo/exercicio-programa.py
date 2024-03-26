# solicitação ao usuário do nome do
def main():
    arquivo=str(input("Escreva o nome do arquivo .txt:"))
    arquivo=open(arquivo, "+") #esse + tá certo?

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
    opcao=int(input("Escolha a opção:"))
    
    #opções para escolha
    if opcao == 1:
        #1. Número de palavras


    elif opcao == 2:
        #2. Número de palavras distintas

    elif opcao == 3:
        #3. Número de linhas

    elif opcao == 4:
        #4. Frequência das palavras

    elif opcao == 5:
        #5. Imprimir uma linha específica

    elif opcao == 6:
        #6. Buscar uma palavra e imprimir a linha em que aparece a primeira ocorrência

    elif opcao == 7:
        #7. Substituir todas as ocorrências de uma palavra por outra

    elif opcao == 8:
        #8. Abrir um outro livro

    elif opcao == 9:
        #9. Encerrar o programa

    #elif opcao == 10: --> SE DER: 10. Gerar nuvem de palavras

    else:
        print("Opção inválida.")


main()