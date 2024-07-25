print ('========== DESAFIO 045 ==========') 
#Crie um programa que faça o computador jogar jokenpô com você
from time import sleep
from random import randint

print('Suas opções: ')
print('[ 0 ] PEDRA ')
print('[ 1 ] PAPEL ')
print('[ 2 ] TESOURA ')
jogador = int(input('Qual a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('-='*20)

itens = ['PEDRA','PAPEL','TESOURA']
computador = randint(0,2)

print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))

print('-='*20)

if computador == 0: #computador jogou PEDRA
    if jogador == 0: #jogador jogou PEDRA
        print('EMPATE!')
    elif jogador == 1: #jogador jogou PAPEL
        print('JOGADOR VENCE!')
    elif jogador == 2: #jogador jogou TESOURA
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1: #computador jogou PAPEL
    if jogador == 0: #jogador jogou PEDRA
        print('COMPUTADOR VENCE!')
    elif jogador == 1: #jogador jogou PAPEL
        print('EMPATE!')
    elif jogador == 2: #jogador jogou TESOURA
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2: #computador jogou TESOURA
    if jogador == 0: #jogador jogou PEDRA
        print('JOGADOR VENCE!')
    elif jogador == 1: #jogador jogou PAPEL
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')

