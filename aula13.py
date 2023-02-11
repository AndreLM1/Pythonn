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
