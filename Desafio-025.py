print ('========== DESAFIO 022 ==========') 
#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nome = str (input('Qual seu nome completo? ')).strip()
print ('Seu nome tem Silva? {}'.format('silva' in nome.lower()))