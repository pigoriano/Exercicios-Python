print ('========== DESAFIO 036 ==========') 
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai eprguntar o valor da casa, o salário do comprador e em quantos anos ele vai calcule o valor da prestação mensal, sabenmdo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$ '))
anos = int (input('Quantos anos de financiamento? '))

prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
