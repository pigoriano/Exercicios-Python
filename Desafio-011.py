print ('========== DESAFIO 011 ==========') 
#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

largura = float(input('Largura da parede:'))
altura = float(input('Altura da parede: '))

dimensao = largura * altura
tinta = dimensao / 2

print('Sua parede tem a dimensão de {:.2f}x{} e sua área é de {:.3f}m².'.format(largura, altura, dimensao))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(tinta))