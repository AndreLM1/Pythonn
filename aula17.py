# Desafio 78
# lista = []
# menor = maior = 0
# for v in range(0, 5):
#     lista.append(int(input('Digite um valor: ')))
#     if v == 0:
#         menor = maior = 0
#     else:
#         if menor > lista[v]:
#             menor = lista[v]
#         if maior < lista[v]:
#             maior = lista[v]
# print('O maior valor é {} e esta nas posições  '.format(maior), end='')
# for i in range(len(lista)):
#     if lista[i] == maior:
#         print('{}°; '.format(i), end='')
# print('\nO menor valor é {} e esta nas posições  '.format(menor), end='')
# for i in range(len(lista)):
#     if lista[i] == menor:
#         print('{}°; '.format(i), end='')

# Desafio 79
# lista = []
# while True:
#     valores = int(input('Digite um valor: '))
#     if valores not in lista:
#         lista.append(valores)
#         print('Valor adicionado!')
#     else:
#         print('Esse valor ja existe! ')

#     sair = str(input('Deseja parar [S/N]? ')).upper()
#     if sair not in 'SsNn':
#         sair = str(input('Deseja parar [S/N]? ')).upper()
#     if sair == 'S':
#         break
# print(sorted(lista))

# Desafio 80
# lista = []
# for v in range(0, 5):
#     valor = int(input('Digite um valor: '))
#     lista.append(valor)
# for i in range(len(lista)):
#     for j in range(len(lista)-1, i, -1):
#         if (lista[j] < lista[j-1]):
#             aux = lista[j]
#             lista[j] = lista[j-1]
#             lista[j-1] = aux
# print(lista)

