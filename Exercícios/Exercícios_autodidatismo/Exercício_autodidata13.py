'''
Leia quatro valores inteiros A, B, C e D.
A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula:
DIFERENCA = (A * B - C * D).
'''

valor_a = float(input('Digite o primeiro valor: '))
valor_b = float(input('Digite o segundo valor: '))
valor_c = float(input('Digite o terceiro valor: '))
valor_d = float(input('Digite o quarto valor: '))

diferenca = (valor_a * valor_b) - (valor_c * valor_d)
print(diferenca)