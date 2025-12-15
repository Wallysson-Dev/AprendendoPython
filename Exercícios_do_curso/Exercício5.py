"""
1º
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
2º
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
3º
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

'''
1º
Chatinho, mas consegui
Erro Lógica
'''

numero_usuario = input ('Informe um número, e eu irei dizer se é par ou impar: ')
verificar = numero_usuario.isdigit()

if verificar:
    numero_int = int(numero_usuario)
    numero_par = numero_int % 2
    numero_impar = numero_int % 2

    if numero_par == 0:
        print (f'O número {numero_int} é par')
    else:
        print (f'O número {numero_int} é impar')
else:
    print ('Isso não é um número inteiro')


'''
2º
Quebrei a cabeça um pouco, com errinhos básicos
Erro Range
'''

hora = input ('Quantas horas são?: ')
verificar = hora.isdigit()

if verificar:
    hora_int = int(hora)

    hora_dia = hora_int >= 0 and hora_int <= 11
    hora_tarde = hora_int >= 12 and hora_int <= 17
    hora_noite = hora_int >= 18 and hora_int <= 23

    if hora_dia:
        print ('Olá bom dia')
    if hora_tarde:
        print ('Olá boa tarde')
    if hora_noite:
        print ('Olá boa noite')
else:
    print ('Isso não é um número')

'''
3º
Erro básico, Syntax
'''

nome_usuario = input ('Qual o seu primeiro nome?: ')
tamanho = len(nome_usuario)

if tamanho <= 4:
    print (f'Seu nome possui {tamanho} letras, então ele é curto')

if tamanho >= 5 and tamanho <= 6:
    print (f'Seu nome tem {tamanho} letras, então ele tem um tamanho normal')

if tamanho > 6:
    print (f'Seu nome tem {tamanho} letras, então ele é grande')


'''
Gostei desses exercícios, mas devo estudar mais:

1- Lógica
2- Criar range
3- Syntax

'''