print ('========== DESAFIO 006 ==========') 
#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = int(input('Digite seu número: '))

dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)

print ('\nAnalizando o valor: {},\nSeu dobro é: {}\nSeu triplo é: {}\nSua Raiz Quadrada é: {:.2f}'.format(n,dobro,triplo,raiz))

#Quebra de linha \n
#Formatar para aparecer 2 digitos após o . {:.2f}