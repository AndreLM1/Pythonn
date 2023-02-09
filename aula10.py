
# Desafio 28
# import random
# numero = random.randint(0,5)
# escolha = int(input('Digite um numero entre 0 e 5: '))
# if escolha == numero:
#     print('Parabens, voce acertou o numero sorteado')
# else:
#     print('Que pena, voce errou, tente dnv!')
# print('\n')
# print('Numero sortido {}. Seu numero escolhido {}'.format(numero, escolha))

# Desafio 29
# vel=float(input('Qual a velocidade do carro: '))
# if vel > 80:
#     multa= (vel-80) * 7 
#     print('Valor da multa R${}'.format(multa))
# else:
#     print('Voce esta dentro do limite de velocidade')

# Desafio 30
# num= float(input('Digite um número: '))
# if (num %2) == 0:
#     print('O numero digitado é par!')
# else:
#     print('O número digitado é ímpar')

# Desafio 31
# dist= float(input('Qual a distância da viagem? '))
# if dist <= 200:
#     preco=  dist * 0.5
#     print('A viagem custará R${:.2f}'. format(preco))
# else:
#     preco= dist  * 0.45
#     print('A viagem custará R${:.2f}'. format(preco))

# Desafio 32
# from datetime import date #Essa biblioteca vai acessar a data e o time do meu pc 
# ano= int(input('Digite o ano que quer analizar? Caso queria analizar  o ano atual, digite 0! '))
# ano= date.today().year
# if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
#     print('O ano {}, é bissexto!'.format(ano))
# else:
#     print('O ano {}, não é bissexto!'.format(ano))


# #Desafio 33
# n1= int(input('Digite o primeiro numero: '))
# n2= int(input('Digite o segundo numero: '))
# n3= int(input('Digite o terceiro numero: '))
# menor = n1 #assumindo que o menor é n1 pois assim elimina um IF
# if n2 < n1 and n2 < n3:
#     menor = n2
# if n3 < n1 and n3 < n2:
#     menor = n3

# maior = n1 #assumindo que o menor é n1 pois assim elimina um IF
# if n2 > n1 and n2 > n3:
#     maior = n2
# if n3 > n1 and n3 > n2:
#     maior = n3

# print('O maior número é {}'.format(maior))
# print('O menor número é {}'.format(menor))
