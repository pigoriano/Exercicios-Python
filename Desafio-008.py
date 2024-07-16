print ('========== DESAFIO 008 ==========') 
#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.

metro = int(input('Digite a quantidade de metros: '))

km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000

print('O valor em km é: {}km'.format(km))
print('O valor em hectometros é: {}hm'.format(hm))
print('O valor em decametro é: {}dam'.format(dam))
print('O valor em decímetro é: {}dm'.format(dm))
print('O valor em centímetros é: {}cm'.format(cm))
print('O valor em milímetros é: {}mm'.format(mm))
