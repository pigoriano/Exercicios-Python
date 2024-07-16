print ('========== DESAFIO 012 ==========') 
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

produto = float(input('Qual é o preço do produto? R$'))

desconto = produto - ( produto * 5 / 100 ) 


print('-'*10)
print ('O produto que custava R${:.2f}, na promoção com edsconto de 5% irá custar R${:.2f}'.format(produto, desconto))
print('-'*10)