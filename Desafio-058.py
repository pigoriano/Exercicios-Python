print ('========== DESAFIO 058 ==========') 
# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
acertou = False
tentativa = 0
computador = randint(0, 10)
print('-=-'*20)
print ('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-'*20)

while not acertou:
    jogador = int (input('Em que número pensei? '))
    tentativa += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print ('Maior... Tente mais uma vez.')
        elif jogador > computador:
            print('Menor... Tente mais uma vez.')

print('PARABÉNS! Você conseguiu me vencer! com {} tentativas.'.format(tentativa))
    
