print ('========== DESAFIO 017 ==========') 
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa

import math

catetoOposto = float(input('Digite o cateto Oposto: '))
catetoAdjacente = float(input('Digite o cateto Adjacente: '))

print('O comprimento da hipotenusa é:{:.2f}'.format(math.hypot(catetoOposto, catetoAdjacente)))
