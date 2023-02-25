#Desafio 66
# n= soma= cont= 0
# print('Caso queira sair do programa, digite 999')
# while True:
#     n=int(input('Digite um valor: '))
#     if n == 999:
#         break
#     soma += n
#     cont += 1
# print('A soma dos {} números vale {}'.format(cont, soma))

#Desafio 67
# while True:
#     num= int(input('Qual tabuda você quer ver? '))
#     if num < 0:
#         break
#     print(10*'-')
#     for c in range (0,11): 
#         mult= num * c
#         print('{} x {} = {}'.format(num, c, mult))    
#     print(10*'-')
# print('Programa encerrado!') 

#Desafio 68
# import random
# print('-----Jogo do Par ou Ímpar-----')
# vitoria= soma= 0
# jogada= '' #defini jogada para fazer a verificação 
# while True:
#     num=int(input('Digite um número: '))
#     jogada= str(input('Par ou Ímpar [P/I]? ')).upper()
#     while jogada not in 'PpIi': #verifica se a jogada digitada está entre P;p;I;i
#         jogada= str(input('Par ou Ímpar [P/I]? ')).upper()
#     pc= random.randint(0,100)
#     if jogada == 'P':
#         if (num + pc) % 2 == 0:
#             soma = num + pc 
#             vitoria += 1
#             print('''{} + {} = {} 
# O número é par, você ganhou!'''.format(num, pc, soma))
#         else:
#             soma = num + pc 
#             print('''{} + {} = {} 
# O número é ímpar, você perdeu!'''.format(num, pc, soma))
#             break
#     if jogada == 'I':
#         if (num + pc) % 2 == 0:
#             soma = num + pc 
#             print('''{} + {} = {} 
# O número é par, você perdeu!'''.format(num, pc, soma))
#             break
#         else:
#             soma = num + pc
#             vitoria += 1
#             print('''{} + {} = {}, 
# O número é ímpar, você ganhou!'''.format(num, pc, soma))
# print('Você ganhou {} vezes'.format(vitoria))

#Desafio 69
# maior= homens= mulheres= 0
# sexo= ''
# while True:
#     # nome= str(input('Digite o nome: '))
#     idade= int(input('Digite a idade: ')) 
#     sexo= str(input('Digite o sexo [M/F]: ')).upper()
#     while sexo not in 'MmFf':
#         sexo= str(input('Digite o sexo [M/F]: ')).upper()
#     sair= str(input('Quer continuar o cadastro [S/N]? ')).upper()
#     while sair not in 'SsNn':
#         sair= str(input('Quer continuar o cadastro [S/N]? ')).upper()
#     if idade >= 18:
#         maior += 1
#     if sexo == 'F' and idade < 20:
#         mulheres += 1
#     elif sexo == 'M':
#         homens+= 1
#     if sair == 'N':
#         break
# print('''Há {} adultos
# Há {} homens
# Há {} mulheres com menos de 20 anos'''.format(maior, homens, mulheres))

#Desafio 70
    

#Desafio Extra
# import random
# vitoria=0
# while True:
#     jogada=int(input('''Escolha sua jogada!
#     [1]- Pedra
#     [2]- Tesoura
#     [3]- Papel
#     '''))
#     pc= random.randint(1,3)
#     if jogada == 1:
#         if pc == 1:
#             print('Pedra x Pedra, empate!')
#         elif pc == 2:
#             vitoria += 1
#             print('Pedra x Tesoura, você ganhou!')
#         else:
#             print('Pedra x Papel, você perdeu, fim de jogo!')
#             break
#     if jogada == 2:
#         if pc == 2:
#             print('Tesoura x Tesoura, empate!')
#         elif pc == 3:
#             vitoria += 1
#             print('Tesoura x Papel, você ganhou!')
#         else:
#             print('Tesoura x Pedra, você perdeu, fim de jogo!')
#             break
#     if jogada == 3:
#         if pc == 3:
#             print('Papel x Papel, empate!')
#         elif pc == 1:
#             vitoria += 1
#             print('Papel x Pedra, você ganhou!')
#         else:
#             print('Papel x Tesoura, você perdeu, fim de jogo!')
#             break
# print('Você teve {} vitórias consecutivas!'.format(vitoria))


    

    
