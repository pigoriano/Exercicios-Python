print ('========== DESAFIO 028 ==========') 
#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o numero escolhido pelo computador
#O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-'*20)
print ('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)

jogador = int (input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('PERDEU! Eu pensei no número: {} e não no {}'.format(computador, jogador))
