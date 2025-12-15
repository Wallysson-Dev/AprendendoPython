'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:
MaiorAB = (a+b+abs(a-b)) / 2
'''

valor_a = float(input('Digite o primeiro valor: '))
valor_b = float(input('Digite o segundo valor: '))
valor_c = float(input('Digite o terceiro valor: '))

MaiorAB = (valor_a + valor_b + abs (valor_a - valor_b)) / 2
Resultado = (MaiorAB + valor_c + abs(MaiorAB - valor_c)) / 2

print(f'O maior valor é {Resultado}')

# Tive q usar o chat, pq tava fazendo as tres verificações tudo numa linha, a formula é de apenas duas