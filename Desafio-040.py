print ('========== DESAFIO 040 ==========') 
#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Media abaixo de 5.0: REPROVADO
#Media entre 5.0 e 6.9: RECUPERAÇÃO
#Média acima de 7: APROVADO

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Você foi REPROVADO!')
elif media >= 5 and media < 7:
    print('Você está de RECUPERAÇÃO!')
else:
    print('Você foi APROVADO!')