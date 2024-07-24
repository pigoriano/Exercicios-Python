print ('========== DESAFIO 038 ==========') 
#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print('o número {} é MAIOR que {}'.format(n1,n2))
elif n1 == n2:
    print('Os números {} e {} tem o mesmo valor'.format(n1,n2))
else:
    print('O número {} é maior que {}'.format(n2,n1))
