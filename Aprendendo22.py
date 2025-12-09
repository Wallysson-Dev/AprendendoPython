"""
Interpolação básica de strings

s - string
d / i - int
f - float
x / X Hexadecimal (ABCDEF/0123456789)
    x minusculo gera minusculo
    X maiusculo gera maiusculo

fstring, .format e interpolação, é basicamente a mesma coisa
"""

nome = 'João'
preco = 2034.5478938
variavel = '%s, o preço total foi de RS' % nome
    # Caso só tenha um '%', não precisa de paresentes

variavel1 = '%s, o preço total foi de RS%f' % (nome, preco)
    # Aqui tem mais de um, então devemos usar parenteses

variavel2 = '%s, o preço total foi de RS%.2f' % (nome, preco)
    # O .X, serve para definir a quantidade de casas decimais que serão exibidas

# Dentro da string deve conter a mesma quantidade que está no "% ()"

print (variavel)
print (variavel1)
print (variavel2)