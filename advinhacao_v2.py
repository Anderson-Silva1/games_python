# Game da advinhação com o WHILE

from random import randint
from time import sleep

number_sort = randint(1, 10)

print('-=-'*20)
print('Vou pensar em um número de 0 a 10, tente adivinhar!...')
print('-=-'*20)

number_jogador = int(input('Escolha um número de 0 a 10: '))

vezes_jogadas = 1

while number_sort != number_jogador:
    if number_jogador > number_sort:
        print('PROCESSANDO...')
        sleep(0.5)
        number_jogador = int(input('MENOS!... Escolha novamente: '))
    else:
        print('PROCESSANDO...')
        sleep(0.5)
        number_jogador = int(input('MAIS!... Escolha novamente: '))
    vezes_jogadas += 1

print('Certa resposta... Eu escolhi o numero {}'.format(number_sort))
print('Você acertou em: {} jogadas!!'.format(vezes_jogadas))
