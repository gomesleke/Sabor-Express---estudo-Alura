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
    '''
    Esse função apenas exibe o nome do app/site
    '''

    print("""
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█\n""")

def options(): 
    '''
    Esta função mostras as opções de acesso
    '''

    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurantes')
    print('4. Sair\n')

def exit_app(): #função de saida
    '''
    Essa função tem com objetivo sair do app/site. 
    Ela tem sistema que simula a saida do usuário através do while
    '''

    repete=0
    os.system('cls') # essa biblioteca limpa o terminal os.system('cls')

    while repete<=2: 
        print('Encerrando...')
        time.sleep(1)
        repete+=1

def back_to_menu():
    '''
    Função que volta pro sisteam de escolhas do menu
    '''
    input('Digite uma tecla para voltar ao menu: ')
    main()

def invalid():
    '''
    Para mostrar que a opção escolhida é inválida
    (essa função surge como forma de otimizar o código)
    '''
    print('Opção Inválida\n')
    back_to_menu()

def sign_up():
    '''
    Basicamente essa função serve para cadrastrar restaurantes na lista, linha #6

    input:
    nome do restaurante
    categoria do restaurante

    output:
    adicona resturanrte na lista
    '''

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
    '''
    Mostra os resuratntes listados por nome/categoria/status de ativação
    '''
    os.system('cls')
    print("""
█░░ █ █▀ ▀█▀ ▄▀█   █▀▄ █▀▀   █▀█ █▀▀ █▀ ▄▀█ █░█ ▀█▀ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀ █▀
█▄▄ █ ▄█ ░█░ █▀█   █▄▀ ██▄   █▀▄ ██▄ ▄█ █▀█ █▄█ ░█░ █▀▄ █▀█ █░▀█ ░█░ ██▄ ▄█\n""")
    
    print(f'{'Nome do Restaurante'.ljust(21)}||{'Categoria'.ljust(20)}||{'Status'}')
    for restaurant in list_restaurants:
        name_print=restaurant['nome']
        category_print=restaurant['categoria']
        status_print='ativo' if restaurant['ativo'] else 'desativado' #ternário
        print(f'-{name_print.ljust(20)}||{category_print.ljust(20)}||{status_print.ljust(20)}')
    
    back_to_menu()

def activate_status():
    '''
    Ativa ou destativa um restaurante do sistema

    input:
    nome do retaurante
    sistema de busca

    output:
    expressar se há o restaurante buscado
    ativar ou desativar
    '''
    os.system('cls')
    print('''
▄▀█ ▀█▀ █▀▀ █▀█ ▄▀█ █▄░█ █▀▄ █▀█   █▀▀ █▀ ▀█▀ ▄▀█ █▀▄ █▀█   █▀▄ █▀█   █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀
█▀█ ░█░ ██▄ █▀▄ █▀█ █░▀█ █▄▀ █▄█   ██▄ ▄█ ░█░ █▀█ █▄▀ █▄█   █▄▀ █▄█   █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄
''')
    name_restaurant=input('Digite o nome do restaurante para alterar o Status: ')
    share_restaurant=False
    repete=0

    for restaurant in list_restaurants:
        if name_restaurant==restaurant['nome']:
            share_restaurant=True
            restaurant['ativo']=not restaurant['ativo']

            process=f'Ativando...' if restaurant['ativo'] else f'Desativando...'
        
            while repete<=2: 
                print(process)
                time.sleep(1)
                repete+=1

        #ternário
            message=f'\nO restaurante {name_restaurant} foi ativado.' if restaurant['ativo'] else f'\nO restaurante {name_restaurant} foi desativado.' 
            print(message)
    if not share_restaurant:
        print('Seu restaurante não está no sistema')

    back_to_menu()

def escolha_opcao():
    '''
    Sistema de escolha do app/site
    '''
    try:
        opcao_escolha=int(input('Escolha uma opção: ')) #sei_la -> snake case (variavel e afins)

        #bool na escolha
        match opcao_escolha:

            case 1:
                sign_up()
            case 2:
                list_print()
            case 3: 
                activate_status()
            case 4:
                exit_app()
            case _:
                invalid()
    except:
        invalid()

def main(): #controla ordem do projeto (para manutenção)
    '''
    Esta função oderna todo o sistema
    '''
    os.system('cls')
    name_program()
    options()
    escolha_opcao()


if __name__=='__main__':  # arquivo principal
    main()