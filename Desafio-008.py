print ('========== DESAFIO 008 ==========') 
#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.

metro = int(input('Digite a quantidade de metros: '))

cm = metro * 100
mm = metro * 1000

print( 'O valor em centímetros é: {}'.format(cm))
print(' O valor em milímetros é: {}'.format(mm))