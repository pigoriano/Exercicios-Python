print ('========== DESAFIO 03 ==========')
#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

variavel = input ('Digite algo: ')
print('O tipo primitivo deste valor é', type(variavel))
print('Só tem espaços?', variavel.isspace())
print ('É um número:', variavel.isnumeric())
print ('É alfabético? ', variavel.isalpha())
print('É um alphanumérico? ', variavel.isalnum())
print ('Está em maiúsculas? ', variavel.isupper())
print ('Está em minúsculas?', variavel.islower())
print ('Está captalizado?', variavel.istitle())
