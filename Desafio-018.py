print ('========== DESAFIO 018 ==========') 
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math

angulo = float(input('Digite um ângulo: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O valor do SENO deste ângulo é: {:.2f}'.format(seno))
print('O valor do COSSENO deste ângulo é: {:.2f}'.format(cosseno))
print('O valor da TANGENTE deste ângulo é: {:.2f}'.format(tangente))