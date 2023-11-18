from random import randint
from time import sleep
from suporte import *

#programa principal
cabecalho()
qtd = quantidade('Quantos participantes?')
pessoas = cadastro(qtd)

tot = len(pessoas)
cont = 0
while cont != tot:
    computador = randint(0, 10)
    print(f'Paricipante {pessoas[cont]["nome"]} tem 3 tentativas')
    for tente in range(1, 4):
        print(f'Tentativa - {tente} ')
        jogador = verificacao('Digite um numero (0 à 10):')
        if jogador < 0:
            break
        sleep(0.8)
        if jogador != computador:
            if computador > jogador:
                print(f'\033[31mVocê perdeu, tente novamente um numero {"\033[33mMAIOR\033[m"}...\033[m')
            else:
                print(f'\033[31mVocê perdeu, tente novamente um numero {"\033[33mMENOR\033[m"}...\033[m')
        else:
            print(f'PARABÉNS {pessoas[cont]['nome']}!, Você ganhou.')
            break
        print('-' * 40)
    cont += 1
print('ola')
