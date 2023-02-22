#Desafio 57
# s= str(input('Digite seu sexo [M/F]: ')).upper()
# while s != 'M' and s != 'F':
#     print('Por favor, digite F ou M')
#     s= str(input('Digite seu sexo [M/F]: ')).upper()

#Desafio 58
# import random
# print('--------JOGO DA ADIVINHAÇÃO--------')
# num= random.randint(0,10)
# n= int(input('Digite um número de 0 a 10: '))
# cont= 1
# while n != num:
#     print('Tente de novo!')
#     n= int(input('Número de 0 a 10: '))
#     cont += 1
# print('Parabéns você adivinhou o número com {} tentativas'.format(cont))

#Desafio 59
# n1= float(input('\033[mDigite um valor: '))
# n2= float(input('Digite um valor: '))
# op= 0
# while op != 5:
#     op= int(input('''Selecione a operação
# [1] soma
# [2] multiplicar
# [3] maior número
# [4] digitar novos números
# [5] sair
#  '''))
#     if op == 1:
#         soma= n1 + n2
#         print('\033[34m {} + {} = {} \033[m'.format(n1,n2,soma))
#     elif op == 2:
#         mult= n1 * n2
#         print('\033[35m{} * {} = {}\033[m'.format(n1,n2,mult))
#     elif op == 3:
#         if n1 > n2:
#             print('\033[36m{} é maior que {}\033[m'.format(n1,n2))
#         elif n1 < n2:
#             print('\033[36m{} é maior que {}\033[m'.format(n2,n1))
#         else:
#             print('\033[36mOs números são iguais!\033[m')
#     elif op == 4:
#          n1= float(input('Digite um valor: '))
#          n2= float(input('Digite um valor: '))

#Desafio 60
# num= int(input('Digite um valor: '))
# cont= num
# fatorial= 1 
# while cont > 0:
#     fatorial= cont * fatorial
#     cont -= 1

# print('fatorial de {} é {}'.format(num,fatorial))

#Desafio 61
# primeiro= int(input('Primeiro termo da p.a: '))
# razao= int(input('Razação da p.a: '))
# cont= 1
# while cont <= 10:
#     print('{} -> '.format(primeiro), end='')
#     primeiro += razao
#     cont += 1
# print('FIM!')

#Desafio 63
# n= int(input('Quantos termos você quer mostrar?  '))
# ultimo= 1
# penultimo= 0
# cont= 3
# print('{} {} '.format(penultimo, ultimo), end='')
# while cont <= n:
    
#     termo= ultimo + penultimo 
#     penultimo= ultimo
#     ultimo= termo
#     cont+= 1
#     print('{} '.format(termo), end='')
    
#Desafio 64
# print('Para sair do programa, por favor digite 999')
# cont= soma= num = 0
# while num != 999:
#     num= int(input('Digite um valor: '))
#     if num != 999:
#         soma += num
#         cont += 1 
# print('''Você digitou {} números
# A soma entre eles é {}'''.format(cont, soma))



