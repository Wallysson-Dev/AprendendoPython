'''
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1,
o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.
'''

codigo_peca = float(input('Digite o código da peça: '))
numero_peca = float(input('Digite quantas peças são: '))
valor_peca = float(input('Digite o valor da peça: '))

pagar = numero_peca * valor_peca
print (f'O valor total a pagar é de R${pagar:,.2f}')