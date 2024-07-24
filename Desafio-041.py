print ('========== DESAFIO 041 ==========') 
#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 20 anos: Sênior
#Acima: MASTER
from datetime import date

nascimento = int(input('Em qual ano você nasceu? '))
atual = date.today().year
idade = atual - nascimento

if idade <= 9:
    print('Você tem {} anos, então está na categoria MIRIM'.format(idade))
elif idade > 9 and idade < 15:
    print('Você tem {} anos, então está na categoria INFANTIL'.format(idade))
elif idade > 15 and idade < 20:
    print('Você tem {} anos, então está na categoria JUNIOR'.format(idade))
elif idade == 20:
    print('Você tem {} anos, então está na categoria SENIOR'.format(idade))
elif idade > 20:
    print('Você tem acima de 20 anos, então está na categoria MASTER!')