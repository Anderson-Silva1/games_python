# Numero sorteado de 0 a 5

# Jogo da advinhação

from random import randint
from time import sleep

print('\033[34m-=-\033[m'*20)
print('\033[33mVou pensar em um número de 0 a 5, tente adivinhar!...\033[m')
print('\033[34m-=-\033[m'*20)

number = int(input("Digite um número de 0 a 5: "))
number_sort = randint(0, 5)

print('\033[33mPROCESSANDO...\033[m')

sleep(3)

if number == number_sort :
    print('\n\033[32mParabens, você acertou o número sorteado!! {}\033[m'.format(number))
else :
    print("\n\033[31mNão foi dessa vêz...\nNúmero sorteado: {}\nSeu número: {}\033[m".format(number_sort, number))

print('\n\033[36mFim de jogo')