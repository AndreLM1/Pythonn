# Desafio 46
# import time
# print('Contagem para estourar os fogos!')
# for c in range(10, -1, -1 ):
#     print(c)
#     time.sleep(1)
# print('BOOOMMMM!')

# Desafio 47
# import time
# for c in range(1, 51):
#     if c % 2 == 0:
#         print(c)
#         time.sleep(0.5)
# print('==================')

# Desafio 48
# soma = 0
# cont = 0
# for c in range(1, 501, 2):
#     if c % 3 == 0:
#         soma = soma + c
#         cont = cont + 1
# print('A soma dos {} números multiplos de 3 é: {}'.format(cont, soma))

# Desafio 49
# num= int(input('Qual tabuada voce quer ver? '))
# for c in range (0, 11):
#     mult= c * num
#     print('{} x {} = {}'.format(num, c, mult))

# Desafio 50
# soma= 0
# for c in range (0,6):
#     num=int(input('Digite um valor: '))
#     if num % 2 == 0:
#         soma = num + soma

# print('A soma de todos os número pares é: {}'.format(soma))

#Desafio 51
# num= int(input('Primeiro termo da p.a: '))
# razao= int(input('Razão da p.a: '))
# decimo= num + (10-1)* razao
# for c in range (num, decimo+1, razao):
#     print('{}'.format(c), end=' -> ')
# print('Acabou!')

#Desafio 52
# num= int(input('Digite um número: '))
# cont= 0
# for c in range(1, num+1):
#     if num % c == 0:
#         cont= cont + 1
#         print('\033[34m', end=' ')
#     else:
#         print('\033[m', end=' ')
#     print('{}'.format(c),'\033[m', end='')
# if cont > 2:
    
#     print('\nO valor digitado não é um número primo, ele foi dividido {} vezes'.format(cont))
# elif cont == 2:
#     print('\nO valor digitado é um número primo, ele foi dividido {} vezes'.format(cont))

#Desafio 53
# frase= str(input('Digite uma frase: ')).strip().upper() #strip tira os espaços do inicio e do final ; upper deixa tudo em maíusculo
# palavra= frase.split() #separando as palavras da frase
# junto= ''.join(palavra) #juntando as palavras sem espaço entre elas
# inverso= ''
# for letra in range(len(junto) -1, -1, -1):
#     inverso= inverso + junto[letra]
# if inverso == junto:
#     print('A frase {} é um palíndromo {}'.format(junto, inverso))
# else:
#     print('{} não é um palíndromo {}'.format(junto, inverso))

#Desafio 54
#from datetime import date
# atual= date.today().year
# maior= 0
# menor= 0
# pessoa=0
# for c in range(0, 7):
#     pessoa+= 1
#     nascimento= int(input('Ano de nascimento da pessoa {}: '.format(pessoa)))
#     idade= atual - nascimento
#     if idade >= 21:
#         maior+= 1
#     else:
#         menor+= 1
# print('Há {} pessoas maiores de idade'.format(maior))
# print('Há {} pessoas menores de idade'.format(menor))

#Desafio 55
# pessoa= 0
# maior= 0 
# menor= 100000
# for c in range(1,6):
#     pessoa+= 1
#     peso= float(input('Peso da pessoa {}: '.format(pessoa)))
#     if peso== 1:
#         maior= peso
#         menor= peso
#     else:
#         if maior < peso:
#             maior= peso
#         if menor > peso:
#             menor= peso
# print('O maior peso é {}kg, e o menor é {}kg'.format(maior, menor))

#Desafio 56
# pessoa= 0
# soma= 0
# maior= 0
# cont= 0
# for c in range(1,5):
#     pessoa+= 1
#     nome= str(input('Nome da {}º pessoa: '.format(pessoa)))
#     idade= int(input('Idade da {}º pessoa: '.format(pessoa)))
#     sexo= str(input('Sexo (M/F) da {}º pessoa: '.format(pessoa))).upper()
#     print('\n')
#     soma += idade
#     if sexo == 'M':
#         if c == 1:
#             maior= idade
#             velho= nome
#         else:
#             if maior < idade:
#                 maior = idade
#                 velho = nome
#     elif sexo== 'F':
#         if idade < 20:
#             cont += 1
#         else:
#             print('Não há mulheres com menos que 20 anos ')


# media= soma/c
# print('A média de idade do grupo é {}'.format(media))
# print('{} é o homem mais velho com {}'.format(velho, maior))
# print('Há {} mulheres com menos de 20 anos'.format(cont))

    