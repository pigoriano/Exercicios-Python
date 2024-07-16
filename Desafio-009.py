print ('========== DESAFIO 009 ==========') 
#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

numero = int(input('Tabuada do número: '))

n0 = numero * 0
n1 = numero * 1
n2 = numero * 2
n3 = numero * 3
n4 = numero * 4
n5 = numero * 5
n6 = numero * 6
n7 = numero * 7
n8 = numero * 8
n9 = numero * 9
n10 = numero * 10

print ('-'*10)
print ('a tabuada do número {} é: '.format(numero))
print ('{} x {:2} = {}'.format(numero, 0,n0))
print ('{} x {:2} = {}'.format(numero, 1,n1))
print ('{} x {:2} = {}'.format(numero, 2,n2))
print ('{} x {:2} = {}'.format(numero, 3,n3))
print ('{} x {:2} = {}'.format(numero, 4,n4))
print ('{} x {:2} = {}'.format(numero, 5,n5))
print ('{} x {:2} = {}'.format(numero, 6,n6))
print ('{} x {:2} = {}'.format(numero, 7,n7))
print ('{} x {:2} = {}'.format(numero, 8,n8))
print ('{} x {:2} = {}'.format(numero, 9,n9))
print ('{} x {:2} = {}'.format(numero, 10,n10))
print ('-'*10)