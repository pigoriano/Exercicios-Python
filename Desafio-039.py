print ('========== DESAFIO 039 ==========') 
#Faça uim programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar
#WSe é a hora de se alistar
#Se ja passou do tempo do alistamento
#Seu programa também deverá mostrar o tempo que falta ou passou do prazo.
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))

idade = atual - nascimento

print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))

if idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Ainda faltam {} anos para sue alistamento'.format(saldo))
    print('Seu alistamento será em {}.'.format(ano))

elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTO!')

elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format( ano))

