print ('========== DESAFIO 013 ==========') 
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Qual o salário do funcionário? R$'))

aumento = salario + (salario*15/100)

print('O funcionário que ganhava R${:.2f}, com aumento de 15%, passa a ganhar R${:.2f}'.format(salario,aumento))