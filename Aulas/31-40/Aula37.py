'''
Tuple - Tupla
É uma lista imutável, ou seja, não pode ser mudada
tupla é melhor que a lista caso não precise alterar nada, já que ela executa mais rápido

Para criar uma tupla, tem dois jeitos
    Ou tiramos os colchetes:
        tupla1 = 'Maria', 'João', 'Joelma'
    Ou utilizamos os parentêses:
        tupla2 = ('Maria', 'João', 'Joelma')
Tupla é resumidamente uma variável(caixa), com várias coisas(presentes) dentro

A função 'tuple(variável)', transforma em uma tuple.
Isso também existe no list, 'list(variável)'
'''

tupla1 = 'Maria', 'João', 'Joelma'
tupla2 = ('Maria', 'João', 'Joelma')

print(type(tupla1))
print(type(tupla2))

lista = ['Maria', 'João', 'Joelma']
lista_para_tuple = tuple(lista)
print(type(lista_para_tuple))