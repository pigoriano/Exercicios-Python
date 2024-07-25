print('========== DESAFIO 044 ==========') 
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
print('========== LOJAS PIGORIANO ==========') 
compra = float(input('Preço das compras: R$'))

print('FORMA DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')

opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = compra - (compra * 10 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(compra, total))
elif opcao == 2:
    total = compra - (compra * 5 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(compra, total))
elif opcao == 3:
    parcela = compra / 2
    print('Sua compra de R${:.2f} será parcelada em 2x de R${:.2f} sem juros'.format(compra, parcela))
elif opcao == 4:
    total = compra + (compra * 20 / 100)
    totalparcela = int(input('Quantas parcelas? '))
    parcela = total / totalparcela
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(totalparcela, parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(compra, total))
else:
    print('Opção inválida, tente novamente!')