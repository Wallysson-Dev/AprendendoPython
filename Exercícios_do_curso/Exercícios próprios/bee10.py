'''
Faça um programa que calcule e mostre o volume de uma esfera
sendo fornecido o valor de seu raio (R). A fórmula para calcular o volume é: (4/3) * pi * R^3.
Considere (atribua) para pi o valor 3.14159.

Dica: Ao utilizar a fórmula, procure usar (4/3.0) ou (4.0/3), pois algumas linguagens (dentre elas o C++),
assumem que o resultado da divisão entre dois inteiros é outro inteiro.
'''

from fractions import Fraction

Fraction (4, 3)

pi = 3.14159
r = int(input('R: '))
float(Fraction (4, 3))

Valor = Fraction (4, 3) * pi * (r**3)
print (Valor)