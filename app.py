# Sabor Express é um tipo de ifood que o curso da alura ensina a construir 
#passo a passo
import time
import os
#fora das funções == global
list_restaurants=[{'nome':'Japones do Japao', 'categoria':'Japonesa','ativo':False},
                  {'nome':'PizzaMil','categoria':'Italiana','ativo':True},
                  {'nome':'McRonald','categoria':'Fastfood','ativo':False}
                  ] #lista de dicionarios // função nova estudada


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

def back_to_menu():
    input('Digite uma tecla para voltar ao menu: ')
    main()

def invalid():
    print('Opção Inválida\n')
    back_to_menu()

def sign_up():
    os.system('cls')
    print("""
█▀▀ ▄▀█ █▀▄ ▄▀█ █▀ ▀█▀ █▀█ █▀█   █▀▄ █▀▀   █▄░█ █▀█ █░█ █▀█ █▀
█▄▄ █▀█ █▄▀ █▀█ ▄█ ░█░ █▀▄ █▄█   █▄▀ ██▄   █░▀█ █▄█ ▀▄▀ █▄█ ▄█

█▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀ █▀
█▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄ ▄█\n""")
    name_restaurant=input('Digite o nome do restaurante para cadastro: ')
    category_restaurant=input(f'Digite a categoria do {name_restaurant}: ')
    
    database_restaurant={'nome':name_restaurant,'categoria':category_restaurant,'ativo':False} #dicionario do cadastro // sempre false o ativo
    list_restaurants.append(database_restaurant)

    print(f'O restaurante {name_restaurant} foi cadastrado com sucesso')
    back_to_menu()

def list_print():
    os.system('cls')
    print("""
█░░ █ █▀ ▀█▀ ▄▀█   █▀▄ █▀▀   █▀█ █▀▀ █▀ ▄▀█ █░█ ▀█▀ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀ █▀
█▄▄ █ ▄█ ░█░ █▀█   █▄▀ ██▄   █▀▄ ██▄ ▄█ █▀█ █▄█ ░█░ █▀▄ █▀█ █░▀█ ░█░ ██▄ ▄█\n""")
    
    for restaurant in list_restaurants:
        name_print=restaurant['nome']
        category_print=restaurant['categoria']
        status_print=restaurant['ativo']
        print(f'-{name_print}||{category_print}||{status_print}')
    
    back_to_menu()

def escolha_opcao():
    try:
        opcao_escolha=int(input('Escolha uma opção: ')) #sei_la -> snake case (variavel e afins)

        #bool na escolha
        match opcao_escolha:

            case 1: 
                print('Cadrastrar Restaurante')
                sign_up()
            case 2:
                print('Listar Restaurantes')
                list_print()
            case 3: 
                print('Ativar Restaurantes')
            case 4:
                exit_app()
            case _:
                invalid()
    except:
        invalid()

def main(): #controla ordem do projeto (para manutenção)
    os.system('cls')
    name_program()
    options()
    escolha_opcao()


if __name__=='__main__':  # arquivo principal
    main()