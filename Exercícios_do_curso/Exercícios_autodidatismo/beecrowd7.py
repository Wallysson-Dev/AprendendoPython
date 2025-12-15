'''
Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas,
o valor que recebe por hora e calcula o salário desse funcionário.
A seguir, mostre o número e o salário do funcionário, com duas casas decimais.
'''

id_func = int(input('Digite seu id: '))
hrs_trabalhadas = float(input('Digite quantas horas você trabalhou: '))
salario_hora = float(input('Digite quanto você ganha por hora: '))

salario = salario_hora * hrs_trabalhadas
print(f'Você recebeu esse mês R${salario:,.2f}')