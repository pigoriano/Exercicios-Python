print ('========== DESAFIO 014 ==========') 
#Crie um conversor de temperatura de Celsius para Fahrenheit

celsius = float(input('Informe a temperatura em °C: '))

f = (celsius * 9/5) + 32

print ('A temperatura de {}°C corresponde a {}°F!'.format(celsius,f))