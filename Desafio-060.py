print ('========== DESAFIO 060 ==========') 
#Faça um programa que leia um npumero qualquer e mostre o seu fatorial.
#Ex: 5! = 5x4x3x2x1= 120

n = int (input('Digite o número a ser fatorado: '))
c = n
f = 1
print ('Calculando {}! = '.format(n), end='')
while c > 0:
    print ('{}'.format(c), end='')
    print (' x ' if c> 1 else ' = ', end='')
    f *= c
    c -= 1 

print ('{}'.format(f))


#solução simples com módulo math
#from math import factorial
#n = int (input('Digite o número para calcular seu Fatorial: '))
#f = factorial (n)
#print ('O fatorial de {} é {}'.format(n,f ))

