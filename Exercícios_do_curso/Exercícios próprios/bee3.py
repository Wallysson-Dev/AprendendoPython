'''
Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores e atribua esta operação à variável PROD.
A seguir mostre a variável PROD com mensagem correspondente.  

Produto/Prod = multiplicação
'''

valor_a = float(input('Digite o primeiro valor: '))
valor_b = float(input('Digite o segundo valor: '))

prod = valor_a * valor_b
print (f'A multiplicação de {valor_a} (*/x) {valor_b} = {prod:,.2f}')