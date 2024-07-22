print ('========== DESAFIO 034 ==========') 
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%
#Para os inferiores ou iguais o aumento é de 15%

salario = int(input('Qual o salario? '))

if salario <= 1250:
    aumento = salario + (salario * 10/100)
    print('Seu salario de R${:.2f} foi aumentado para R${:.2f}'.format(salario,aumento))
else:
    aumento = salario + (salario * 15/100)
    print('Seu salário de R${:.2f} foi aumentado para R${:.2f}'.format(salario,aumento))