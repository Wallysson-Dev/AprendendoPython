'''
Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro).
Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
informar o total a receber no final do mês, com duas casas decimais.
'''

nome_func = input('Digite seu nome: ')
salario_fixo = float(input('Digite seu salário fixo: '))
vendas_efetuadas = float(input('Quanto você vendeu esse mês(em dinheiro): '))

bonus = ((vendas_efetuadas / 100) * 15) + salario_fixo
print(f'Seu salário esse mês foi de R${bonus:,.2f}')