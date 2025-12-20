# Sabor Express é um tipo de ifood que o curso da alura ensina a construir 
#passo a passo
import time
import os

def name_program():
    print("""
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█\n""")

def options():  
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurantes')
    print('4. Sair\n')

def exit_app(): #função de saida
    repete=0
    os.system('cls') # essa biblioteca limpa o terminal os.system('cls')

    while repete<=2: 
        print('Encerrando...')
        time.sleep(1)
        repete+=1

def escolha_opcao():
    opcao_escolha=int(input('Escolha uma opção: ')) #sei_la -> snake case (variavel e afins)


    #bool na escolha
    match opcao_escolha:

        case 1: 
            print('Cadrastrar Restaurante')
        case 2:
            print('Listar Restaurantes')
        case 3: 
            print('Ativar Restaurantes')
        case 4:
            exit_app()
        case _:
            print("Inválido")

def main(): #controla ordem do projeto (para manutenção)
    name_program()
    options()
    escolha_opcao()


if __name__=='__main__':  # arquivo principal
    main()