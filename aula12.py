# ctrl + K + C para comentar multiplas linhas
# Desafio 36
# valor=float(input('Qual o valor da casa? R$'))
# salario=float(input('Qual o seu salário? R$'))
# anos=int(input('Quantos anos de financiamento?'))
# prestacao= valor/(anos*12)
# print('Valor da prestação: R${:.2f}'.format(prestacao))
# if prestacao > (salario*0.3):
#     print('A prestação é 30% maior que seu salário, portanto, você não receberá o empréstimo!')
# else:
#     print('Você receberá seu empréstimo!')


# Desafio 37
# num= int(input('Digite um número inteiro: '))
# print('\n')
# choice=int(input('''Digite [1] para converter o número em binário;
# Digite [2] para converter em octal;
# Digite [3] para converter em hexadecimal:\nEscolha: '''))
# if choice == 1:
#     type='Binário'
#     convert= bin(num)
#    elif choice ==2:
#     type='Octal'
#     convert= oct(num)
# else:
#     type='Hexadecimal'
#     convert= hex(num)
# print('O numero {}, convertido para {} é {}'.format(num,type,convert[2:])) #[2:] é para printar sem o código do tipo de caracter
#                                                                             #exemplo binario aparece como 0b

# Desafio 38
# n1=int(input('Digite um valor: '))
# n2=int(input('Digite outro valor: '))

# if n1 > n2:
#     print('{} é maior que {}'.format(n1,n2))
# elif n1 < n2:
#     print('{} é maior que {}'.format(n2, n1))
# elif n1 == n2:
#     print('Os dois números são iguáis!')

# Desafio 39
# from datetime import date
# idade=int(input('Quantos anos voce tem? '))
# ano_atual= date.today().year
# if idade < 18:
#     ano_nascimento= ano_atual - idade
#     alistamento= 18 - idade
#     anos_alista=ano_nascimento + idade
#     print('Faltam {} anos para seu alistamento. Ele ocorrera em {}'.format(alistamento, anos_alista))
# elif idade == 18:
#     print('Você terá que se alista nesse ano de {}'.format(ano_atual))
# else:
#     ano_nascimento= ano_atual - idade
#     passou= ano_atual- (ano_nascimento + 18)
#     print('Se passaram {} anos do seu alistamento'.format(passou))

# Desafio 40
# n1 = float(input('1º nota: '))
# n2 = float(input('2º nota: '))
# med = (n1+n2)/2
# if med < 5:
#     print('Média: {:.2f}'.format(med))
#     print('REPROVADO!')
# elif (med > 5) and (med < 6.9):
#     print('Média: {:.2f}'.format(med))
#     print('RECUPERAÇÃO!')
# elif med >= 7:
#     print('Média: {:.2f}'.format(med))
#     print('APROVADO!')

# Desafio 41
# from datetime import date
# ano_nas= int(input('Ano em que nasceu: '))
# ano_atual= date.today().year
# print('Idade: {}'.format(ano_atual - ano_nas))
# if (ano_atual - ano_nas) <= 9:
#     print('CATEGORIA [ MIRIM ]')
# elif (ano_atual - ano_nas) > 9 and (ano_atual - ano_nas) <= 14:
#     print('CATEGORIA [ INFANTIL ]')
# elif (ano_atual - ano_nas) > 14 and (ano_atual - ano_nas) <= 19:
#     print('CATEGORIA [ JÚNIOR ]')
# elif (ano_atual - ano_nas) > 19 and (ano_atual - ano_nas) <= 25:
#     print('CATEGORIA [ SÊNIOR ]')
# elif (ano_atual - ano_nas) > 25:
#     print('CATEGORIA [ MÁSTER ]')

# Desafio 42
# l1 = float(input('Digite um lado do triangulo '))
# l2 = float(input('Digite um lado do triangulo '))
# l3 = float(input('Digite um lado do triangulo '))
# if l1 < (l2+l3) and l2 < (l1 + l3) and l3 < (l1 + l2):
#     print('Com essas medidas é possível fazer um triangulo')
#     if (l1 == l2) and (l2 == l3):
#         print('TRIÂNGULO EQUILÁTERO')
#     elif ((l1 == l3) and (l3 != l2)) or ((l2 == l1) and (l1 != l3)):
#         print('TRIÂNGULO ISÓCELES')
#     elif(l1 != l2) and (l2 != l3) and (l1 != l3):
#         print('TRIÂNGULO ESCALENO')

# else:
#     print('Nâo é possível fazer um triangulo com essas medidas!')

#Desafio 43
# peso=float(input('Peso(kilog): '))
# altura=float(input('Altura(metros):  '))
# imc= peso/(altura**2)
# print('IMC:{:.2f}'.format(imc))
# if imc =< 18.5:
#     print('ABAIXO DO PESO')
# elif imc > 18.5 and imc < 25:
#     print('PESO IDEAL')
# elif imc >= 25 and imc < 30:
#     print('SOBREPESO')
# elif imc >= 30 and imc <40:
#     print('OBESIADE')
# else:
#     print('OBESIADE MÓRBIDA')

#Desafio 44
# preco= float(input('Valor da compra: R$'))
# tipo=int(input('''Selecione o tipo de pagamento
# [1] Pagamento à vista no dinheiro/cheque
# [2] Pagamento à vista no cartão
# [3] Pagamento em até 2x sem juros
# [4] Pagamento em até 3x ou mais com juros de 20%
#  '''))
# if tipo == 1:
#     desc= preco*0.9
#     print('''Você tem 10% de desconto
#     Valor final: R${:.2f}'''.format(desc))
# elif tipo == 2:
#     desc= preco*0.95
#     print('''Você tem 5% de desconto
#     Valor final: R${}'''.format(desc))
# elif tipo == 3:
#     parcela= preco/2
#     print('Valor final: 2x de R${:.2f}'.format(parcela))
# elif tipo == 4:
#     parcela= int(input('Quanta parcelas? '))
#     final= (preco/parcela)*1.2
#     preco= preco*1.2
#     print('''Valor final: {}x de R${:.2f}
# No total você pagará: R${}'''.format(parcela, final,preco))
# else:
#     print('Opção inválida!')

#Desafio 45
# import random
# jogada=int(input('''Escolha sua jogada!
# [1] - Pedra
# [2] - Papel
# [3] - Tesoura
# '''))
# jogada_pc = random.randint(1,3)
# if jogada == jogada_pc:
#     if jogada == 1 and jogada_pc == 1:
#         print('''Pedra x Pedra
# EMAPTE!''') 
#     elif jogada == 2 and jogada_pc == 2:
#         print('''Papel x Papel
# EMAPTE!''')        
#     elif jogada == 3 and jogada_pc == 3:
#         print('''Tesoura x Tesoura
# EMAPTE!''')        
# elif (jogada == 1) and (jogada_pc == 2):
#     print('''Pedra x Papel
# DERROTA!''')
# elif (jogada == 1) and (jogada_pc == 3):
#     print('''Pedra x Tesoura
# VITÓRIA!''')
# elif (jogada == 2) and (jogada_pc == 1):
#     print('''Papel x Pedra
# VITÓRIA!''')
# elif (jogada == 2) and (jogada_pc == 3):
#     print('''Papel x Tesoura
# DERROTA!''')
# elif (jogada == 3) and (jogada_pc == 1):
#     print('''Tesoura x Pedra
# DERROTA!''')
# elif (jogada == 3) and (jogada_pc == 2):
#     print('''Tesoura x Papel
# VITÓRIA!'''.format(jogada, jogada_pc))