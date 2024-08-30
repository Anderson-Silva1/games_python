# Jo Ken Po

from time import sleep
from random import randint
item = ("Pedra", 'Papel', 'Tesoura')
escolha_maquina = randint(0, 2)
print("""Escolha uma das opções:
[0] - Pedra
[1] - Papel
[2] - Tesoura""")
escolha_jogador = int(input('Escolha do jogador '))

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')

print('-=-'*20)
print('O computador escolheu \033[34m{}\033[m'.format(item[escolha_maquina]))
print('O jogador escolheu \033[34m{}\033[m'.format(item[escolha_jogador]))
print('-=-'*20)

if escolha_maquina == 0: # Máquina escolhe PEDRA
    if escolha_jogador == 0:
        print('\033[1;33mEMPATE!\033[m')
    elif escolha_jogador == 1:
        print('\033[1;32mO Jogador ganhou!!!\033[m')
    elif escolha_jogador == 2:
        print('\033[1;31mA Máquina ganhou!!!\033[m')
    else:
        print('Opção inválida')

elif escolha_maquina == 1: # Máquina escolhe PAPEL
    if escolha_jogador == 1:
        print('\033[1;33mEMPATE!\033[m')
    elif escolha_jogador == 2:
        print('\033[1;32mO Jogador ganhou!!!\033[m')
    elif escolha_jogador == 0:
        print('\033[1;31mA Máquina ganhou!!!\033[m')
    else:
        print('Opção inválida')

elif escolha_maquina == 2: # Máquina escolhe TESOURA
    if escolha_jogador == 2:
        print('\033[1;33mEMPATE!\033[m')
    elif escolha_jogador == 0:
        print('\033[1;32mO Jogador ganhou!!!\033[m')
    elif escolha_jogador == 1:
        print('\033[1;31mA Máquina ganhou!!!\033[m')
    else:
        print('Opção inválida')

