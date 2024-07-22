print ('========== DESAFIO 029 ==========') 
#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma msg dizendo que ele foi multado
#A multa vai custar R$7,00 por cada km acima do limite.

import math
velocidade = int(input('Qual a velocidade atual do carro?'))

if velocidade >= 81:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')