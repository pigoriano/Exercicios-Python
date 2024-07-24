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
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Você tem {} anos, então está na categoria MIRIM'.format(idade))
elif idade <=14:
    print('Você tem {} anos, então está na categoria INFANTIL'.format(idade))
elif idade <=19:
    print('Você tem {} anos, então está na categoria JUNIOR'.format(idade))
elif idade <=25:
    print('Você tem {} anos, então está na categoria SENIOR'.format(idade))
else:
    print('Você tem acima de 25 anos, então está na categoria MASTER!')