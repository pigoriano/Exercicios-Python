print ('========== DESAFIO 049 ==========') 
#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input('Digite um número para ver sua tabuada: '))
for contador in range(0,10):
    print('{} X {:2} = {}'.format(numero, contador, contador*numero))