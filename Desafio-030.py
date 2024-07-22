print ('========== DESAFIO 030 ==========') 
#Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar

import math
numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2

if resultado == 1:
    print('O número {} é IMPAR'.format(numero))
else:
    print('O número {} é PAR'.format(numero))