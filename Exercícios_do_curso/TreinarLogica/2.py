'''
Exercicios para aprender mais aprofundadamente usar 'for in'

1- Percorra uma lista e imprima só os números pares

2- Some todos os valores de uma lista

3- Conte quantos números são maiores que 10

Exercicios do chatGPT
(Utilizo o chatGPT para que eu possa tirar duvidas, ele cria exercicios sobre o assunto para que eu resolva)
'''

# 1-

# for numero in range(1, 51):
#     if numero % 2 == 0:
#         print(f'{numero} esse número é par')
#     else:
#         print (f'{numero} esse número é ímpar')

# 2.1-

# soma = 0
# for num in range(1, 51):
#     if num % 2 == 0:
#         soma += num
#         print(soma)

# 2.2-
# soma = 0
# for num in range(1, 51):
#     if num % 2 == 0:
#         soma += num
#         print(soma)# -> quando quiser ver o processo, coloca o print dentro do bloco e, quando quiser ver o resultado final, coloca o print fora do bloco

# 2.3-

# soma = 0
# for num in range (1, 51):
#     if num % 3 == 0 or num % 5 == 0:
#         soma += num

# print (soma)

# 2.4-

# contador = 0
# for num in range (1, 101):
#     if num % 4 == 0 or num % 6 == 0:
#         contador += 1
# print(contador)

# 2.5-

# soma = 0
# for num in range (1, 101):
#     if num % 2 == 1 and num % 5 == 0:
#         soma += num

# print (soma)

# 3-

# contador = 0
# for num in range (1, 51):
#     if num > 10:
#         contador += 1
# print (contador)