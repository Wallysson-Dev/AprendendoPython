# Input, serve para coletar os dados do usuário
# input('Qual seu nome? ')

# Para coletar os dados e por numa variável
nome = input('Qual seu nome? ')
print (f'O seu nome é {nome=}')# Quando tiver um sinal de igual dentro da chave, o código mostra o nome da variável
# Assim, o dado é coletado, e colocado dentro da variável

n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')

print (f'A soma dos números é: {n1 + n2}')# Aqui irá mostrar o resultado errado
# O input transforma tudo em str
# E str + str, gera uma concatenação, ou seja, uma junção

#  n1 = int(input('Digite um número: '))
#  n2 = int(input('Digite outro número: '))
# Converter já aqui, pode gerar um transtorno, pois caso o usuário escreva algo que não pode ser transformado em int, o código quebra