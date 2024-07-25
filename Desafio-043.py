print ('========== DESAFIO 043 ==========') 
#Desenvolva uma logica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5: Abaixo do peso
#Entre 18.5 e 25: Peso ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade mórbida

peso = float (input('PESO (Kg): '))
altura = float (input('ALTURA (m): '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print ('Você está ABAIXO DO PESO | SEU IMC: {:.1f} '.format(imc))
elif imc > 18.5 and imc <= 24.9:
    print ('Você está no PESO IDEAL | SEU IMC: {:.1f} '.format(imc))
elif imc >= 25 and imc < 29.9:
    print ('Você está com SOBRE PESO | SEU IMC: {:.1f} '.format(imc))
elif imc > 30 and imc < 39.9:
    print ('Você está com OBESIDADE | SEU IMC: {:.1f} '.format(imc))
elif imc > 40:
    print ('Você está com OBESIDADE MÓRBIDA | SEU IMC: {:.1f} '.format(imc))