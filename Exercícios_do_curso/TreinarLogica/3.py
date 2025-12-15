"""
1 — Criar e acessar lista
Crie uma lista com 5 números digitados pelo usuário.
Depois:
mostre a lista inteira
mostre apenas o primeiro e o último número

2 — Percorrer uma lista
imprimir cada número
imprimir se ele é par ou ímpar

3 — Somar valores de uma lista
calcule a soma dos valores
mostre o resultado final

4 — Criar uma nova lista (filtro)
Crie outra lista contendo apenas os números maiores que 10

5 — Modificar uma lista
multiplicar cada número por 2
atualizar a própria lista
"""

# 1-

i = 0
lista = []
while i < 5:
    lista.append(input("Digite um valor: "))
    i += 1

print(f"{lista}, lista inteira")
print(f"Primeiro número é {lista[0]}")
print(f"Ultimo número é {lista[-1]}")

# 2-

lista = [3, 6, 4, 8, 19, 71, 49]
for numero in lista:
    print(numero)
    if numero % 2 == 0:
        print(f"O número {numero} é par")
    else:
        print(f"O número {numero} é ímpar")

# 3-

lista = [3, 6, 4, 8, 19, 71, 49]
soma = 0

for numero in lista:
    soma += numero

print("-" * 30)
print(f"Os números são {lista}")
print("-" * 30)
print(f"A soma dos numeros é {soma}")

# 4-

lista_total = [8, 100, 5, 61, 34, 37, 95, 40, 3, 7, 4, 2, 6, 9]
lista_M10 = []

for numero in lista_total:
    if numero > 10:
        lista_M10.append(numero)
print(lista_M10)

# 5-

lista = [8, 100, 5, 61, 34, 37, 95, 40, 3, 7]
i = 0

for i in range(len(lista)):
    lista[i] = lista[i] * 2

print(lista)

# ANOTAÇÕES IMPORTANTES SOBRE LISTAS (APRENDIZADO)
#
# 1) Se eu quero acumular valores em uma lista, ela deve ser criada FORA do for.
#
# 2) Nunca devo alterar o tamanho da lista (append/insert)
#    enquanto percorro ela com for.
#
# 3) append() adiciona UM elemento
#    extend() adiciona VÁRIOS elementos
#    insert() insere em uma posição específica
#
# 4) Variáveis acumuladoras (soma, contador, listas)
#    devem ser criadas antes do laço.
#
# 5) Para LER valores da lista:
#    for valor in lista
#
# 6) Para ALTERAR valores da lista:
#    for i in range(len(lista))
#        lista[i] = novo_valor
#
# Errar faz parte do aprendizado.
# O importante é entender o erro e corrigir a lógica.
