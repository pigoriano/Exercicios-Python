print ('========== DESAFIO 03 ==========')
#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

variavel = input ('Digite algo: ')
print('O tipo é', type(variavel))
print('É um número? ', variavel.isalnum())
print ('É alphanumérico? ', variavel.isalpha())