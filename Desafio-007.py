print ('========== DESAFIO 007 ==========') 
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostrea a sua média.

nota1 = float(input('Qual foi a nota da Primeira prova? '))
nota2 = float(input('Qual foi a nota da Segunda prova? '))

media = (nota1 + nota2) / 2

print('A média entre {:.1f} e {:.1f} é igual a: {:.1f}'.format(nota1,nota2,media))

5