'''
Treino de Lógica
Dia 4 e 5

Exercício 1 - D4 — Contar positivos
Dada uma lista de números, conte quantos são maiores que zero.

Exercício 2 - D4 -Maior valor
Dada uma lista de números, encontre o maior valor

Exercício 3 — D4 - Menor valor
Dada uma lista de números, encontre o menor valor

Exercício 4 — D4 - Soma dos pares
Dada uma lista, some apenas os números pares.

Exercício 5 — D4 - Lista de ímpares
Dada uma lista, crie outra lista apenas com os números ímpares.

--------------------------------------------------------------------------------

Exercício 1 — D5 - Contar múltiplos
Conte quantos números da lista são múltiplos de 3.

Exercício 2 — D5 - Média simples
Calcule a média dos valores de uma lista

Exercício 3 — D5 - Substituição condicional
Dada uma lista, substitua:
números menores que 10 por 0
números maiores ou iguais a 10 permanecem
A lista deve ser modificada, não criar outra.

Exercício 4 — D5 - Verificação
Dada uma lista, verifique se existe pelo menos um número negativo.
Imprima:
"Existe número negativo" ou
"Não existe número negativo"

Exercício 5 — D5 - Contagem combinada (desafio leve)
Conte quantos números da lista são:
pares e
maiores que 20
'''


#--------------------------------------------------------------------------------

# Exercício 1 - D4 - Contar positivos
# Dada uma lista de números, conte quantos são maiores que zero.

# contador = 0
# lista = [14, 5, 6, 4, 90, 19, 3, 1, 79, 51, 54, 7, 23, 2, 9, 30, 48, 13, 8]

# for num in lista:
#     if num > 10:
#         contador += 1
# print(f'Dentro da lista, tem {contador} números maiores que 10')

#--------------------------------------------------------------------------------

# Exercício 2 - D4 - Maior valor
# Dada uma lista de números, encontre o maior valor

# lista = [14, 5, 6, 4, 90, 19, 3, 1, 79, 51, 54, 7, 23, 2, 9, 30, 48, 13, 8]
# num_maior = 0

# for num_atual in lista:
#     if num_atual > num_maior:
#         num_maior = num_atual
# print(f'O maior número da lista é {num_maior}')

#--------------------------------------------------------------------------------

# Exercício 3 - D4 - Menor valor
# Dada uma lista de números, encontre o menor valor

# lista = [14, 5, 6, 4, 90, 19, 3, 1, 79, 51, 54, 7, 23, 2, 9, 30, 48, 13, 8]
# num_menor = lista[0]

# for num_atual in lista:
#     if num_atual < num_menor:
#         num_menor = num_atual
# print(f'O menor número da lista é {num_atual}')

#--------------------------------------------------------------------------------

# Exercício 4 - D4 - Soma dos pares
# Dada uma lista, some apenas os números pares.

# lista = [14, 5, 6, 4, 90, 19, 3, 1, 79, 51, 54, 7, 23, 2, 9, 30, 48, 13, 8]
# soma = 0

# for num in lista:
#     if num % 2 == 0:
#         soma += num
# print (soma)

#--------------------------------------------------------------------------------

# Exercício 5 - D4 - Lista de ímpares
# Dada uma lista, crie outra lista apenas com os números ímpares.

# lista = [14, 5, 6, 4, 90, 19, 3, 1, 79, 51, 54, 7, 23, 2, 9, 30, 48, 13, 8]
# impar = 0
# lista_impar = []

# for num in lista:
#     if num % 2 == 1:
#         lista_impar.append(num)
# print(lista_impar)

#--------------------------------------------------------------------------------

# Exercício 1 — D5 - Contar múltiplos
# Conte quantos números da lista são múltiplos de 3.

# lista = [14, 5, 6, 4, 90, 19, 3, 1, 79, 51, 54, 7, 23, 2, 9, 30, 48, 13, 8]
# contador_multiplo = 0

# for num in lista:
#     if num % 3 == 0:
#         contador_multiplo += 1
# print (f'A quantidade de números multiplos de 3 é {contador_multiplo}')

#--------------------------------------------------------------------------------

# Exercício 2 — D5 - Média simples
# Calcule a média dos valores de uma lista

# lista = [14, 5, 6, 4, 90, 19, 3, 1, 79, 51, 54, 7, 23, 2, 9, 30, 48, 13, 8]
# soma_lista = 0

# for num in lista:
#     soma_lista += num
# divisao_lista = soma_lista / len(lista)
# print(f'A média dos números da lista é de {divisao_lista:,.2f}')

#--------------------------------------------------------------------------------

# Exercício 3 — D5 - Substituição condicional
# Dada uma lista, substitua:
# números menores que 10 por 0
# números maiores ou iguais a 10 permanecem
# A lista deve ser modificada, não criar outra.

# lista = [14, 5, 6, 4, 90, 19, 3, 1, 79, 51, 54, 7, 23, 2, 9, 30, 48, 13, 8]
# substituir = 0
# i = 0

# for num in lista:
#     if num > 10:
#         lista[i] = substituir
#     i += 1
# print (lista)

#--------------------------------------------------------------------------------

# Exercício 4 — D5 - Verificação
# Dada uma lista, verifique se existe pelo menos um número negativo.

# lista = [14, 5, 6, 4, 90, 19, 3, 1, 79, 51, 54, 7, 23, -2, 9, 30, 48, 13, 8]

# for num in lista:
#     if num < 0:
#         print (f'Na lista possui número negativo, sendo ele {num}')
# print(lista)

#--------------------------------------------------------------------------------

# Exercício 5 — D5 - Contagem combinada (desafio leve)
# Conte quantos números da lista são:
# pares e maiores que 20

# lista = [14, 5, 6, 4, 90, 19, 3, 1, 79, 51, 54, 7, 23, -2, 9, 30, 48, 13, 8]
# contador = 0

# for num in lista:
#     if num % 2 == 0 and num > 20:
#         contador += 1
# print (f'Existem {contador} números que são pares e maiores que 20')

#--------------------------------------------------------------------------------

# ----------------- RESUMO DOS EXERCÍCIOS (ERROS E APRENDIZADO) -----------------
#
# Principais erros cometidos:
# - Em alguns exercícios usei a condição errada (ex: > 10 em vez de > 0),
#   mostrando a importância de ler o enunciado com mais atenção.
# - Inicializei o maior valor com 0; funcionou, mas aprendi que o correto
#   é iniciar com o primeiro elemento da lista.
# - Em um exercício imprimi a variável errada, reforçando a necessidade
#   de atenção aos nomes das variáveis.
# - Inverti a lógica em uma substituição condicional (zerei valores errados)
#   mostrando mais uma vez a importância de ler o enunciado com mais atenção.
# - Tive dificuldade em exercícios de verificação, após a correção das questões aprendi a usar
#   uma variável de controle (flag) e decidir fora do laço é mais correto.
#
# Como posso melhorar:
# - Ler o problema com calma antes de programar.
# - Pensar no objetivo final antes de escrever o for.
# - Revisar condições e variáveis antes de imprimir resultados.
# - Praticar mais exercícios de controle de fluxo e verificação.
#
# Conclusão:
# Os exercícios de hoje ajudaram a consolidar lógica de programação.
# Os erros fizeram parte do aprendizado e me ajudaram a entender melhor
# o fluxo do código e a tomar decisões mais corretas.
#
# Aceito FeedBack :)
# -----------------------------------------------------------------------------
