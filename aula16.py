# Desafio 72
# numeros= ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
#            'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
#            'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
#            'dezessete', 'dezoito', 'dezenove', 'vinte')
# while True:
#     num= int(input('Digite um valor entre 0 e 20: '))
#     if 0 <= num <= 20:
#         break
# print('Você digitou o número \033[35m{}\033[m '.format(numeros[num]))

# Desafio 73
# brasileirao= ('Palemiras','Internacional','Fluminense','Corinthians',
#               'Flamengo','Atlético Paranaense','Atlético Mineiro',
#               'Fortaleza','São Paulo','América',
#               'Botafogo','Santos','Goias','RedBUll','Coritiba',
#               'Cuiabá','Ceará','Atlético','Avaí','Juventude')
# print('Os 5 primeiros colocados são: {}'.format(brasileirao[0:5]))
# print('Os 4 útimos colocados são: {}'.format(brasileirao[16:20]))
# print(sorted(brasileirao))
# print('Coritiba está em {}º no brasileirão'.format(brasileirao.index('Coritiba')+1))

# Desafio 74
# import random
# menor= 10000000
# maior= 0
# num=(random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10))
# for c in range(0, len(num)):
#     if num[c] < menor:
#         menor= num[c]
#     if num[c] > maior:
#         maior= num[c]
# print('''{}
# Maior número: {}
# Menor número: {}'''.format(num, maior, menor))

# Desafio 75
# num= (int(input('Digite um valor: ')),
#       int(input('Digite um valor: ')),
#       int(input('Digite um valor: ')),
#       int(input('Digite um valor: ')))
# print('Os números digitados foram:', end=' ')
# for c in num:
#     if c % 2 == 0:
#         print(c , end=' ')
# print('\nO numero 9 apareceu {} vezes'.format(num.count(9)))
# if 3 in num:
#     print('O primeiro num 3 digitado está na posição {}'.format(num.index(3)+1))
# else:
#     print('O número 3 não foi digitado!')

# Desafio 77
# text = ('carro', 'barco', 'moto', 'uber')
# for c in text:
#     print('\nIn {} the vowels are:'.format(c), end=' ')
#     for g in c:
#         if g in 'aeiou':
#             print(g, end=' ')
            
