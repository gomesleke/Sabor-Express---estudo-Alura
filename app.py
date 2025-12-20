# Sabor Express é um tipo de ifood que o curso da alura ensina a construir 
#passo a passo
import time
import os

print("""
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█\n""")

print('1. Cadastrar Restaurante')
print('2. Listar Restaurantes')
print('3. Ativar Restaurantes')
print('4. Sair\n')

opcao_escolha=int(input('Escolha uma opção: ')) #sei_la -> snake case (variavel e afins)


#bool na escolha

def exit_app(): #função de saida
    repete=0
    os.system('cls') # essa biblioteca limpa o terminal os.system('cls')

    while repete<=2: 
        print('Encerrando...')
        time.sleep(1)
        repete+=1

if opcao_escolha==1:
    print('Cadrastrar Restaurante')
elif opcao_escolha==2:
    print('Listar Restaurantes')
elif opcao_escolha==3:
    print('Ativar Restaurantes')
else:
    exit_app()