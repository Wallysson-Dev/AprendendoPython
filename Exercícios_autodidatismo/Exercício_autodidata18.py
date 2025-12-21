'''
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.
'''

valor_a = float(input('Digite o primeiro valor: '))
valor_b = float(input('Digite o segundo valor: '))
valor_c = float(input('Digite o terceiro valor: '))

# Base = valor_a
# Altura = valor_c

# A) A área do triângulo retângulo que tem A por base e C por altura.
area_triangulo_retangulo = (valor_a * valor_c) / 2
print(f'A área do triângulo retângulo é de {area_triangulo_retangulo}cm²')


# B) A área do círculo de raio C. (pi = 3.14159)
pi = 3.14159
area_circulo = area_c = pi * (valor_c ** 2)
print (f'A área do circulo é de {area_circulo}cm²')


# C) a área do trapézio que tem A e B por bases e C por altura.
area_trapezio = ((valor_a + valor_b) * valor_c) / 2
print (f'A área do trapezio é de {area_trapezio}cm²')


# D) a área do quadrado que tem lado B.
area_quadrado = area_q = valor_b ** 2
print (f'A área do quadrado é de {area_quadrado}cm²')


# E) a área do retângulo que tem lados A e B.
area_retangulo = area_r = valor_a * valor_b
print (f'A área do retângulo é de {area_retangulo}cm²')