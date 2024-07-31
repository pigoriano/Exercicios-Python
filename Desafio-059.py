print ('========== DESAFIO 059 ==========') 
# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0
from time import sleep
while opcao != 5:
    print('-=-'*20)
    print('[ 1 ] SOMAR ')
    print('[ 2 ] MULTIPLICAR ')
    print('[ 3 ] MAIOR')
    print('[ 4 ] NOVOS NÚMEROS')
    print('[ 5 ] SAIR DO PROGRAMA')
    print('-=-'*20)
    opcao = int(input('Qual é a opção? '))

    if opcao == 1:
        soma = n1+n2
        print('A soma de {} + {} é = {}'.format(n1,n2,soma))
    elif opcao == 2:
        multiplicar = n1 * n2
        print('A multiplicação de {} x {} é = {}'.format(n1,n2,multiplicar))    
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('Entre {} e {}, o maior valor é: {}'.format(n1,n2,maior))
        else:
            maior = n2
            print('Entre {} e {}, o maior valor é: {}'.format(n1,n2,maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    
    elif opcao == 5:
        print ('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida. Tente novamente')

print('Fim do programa! Volte sempre!')