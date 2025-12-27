'''
Empacotamento e Desempacotamento - Introdução

Imagine que o list(ou qualquer outro iterável) é um pacote
            0         1        2
lista = ['Maria', 'Helena', 'João']
    O que fica dentro das chaves([...]) está 'empacotado'
Para 'desempacotar', a lista deve ser atribuida a variáveis
    Exemplo:
        nome0, nome1, nome2 = lista
        Os 'itens' da lista serão atribuidos respectivamente
        Ou seja, nome0 = 'Maria'
                 nome1 = 'Helena'
                 nome2 = 'João'

Para pegar apenas um item da lista:
    nome0, *resto = lista
    nome0 = 'Maria'
    resto = ['Helena', 'João']
A variável 'resto normalmente não é utilizada
Quanto criamos uma variável e não utilizamos, deixamos o nome da variável de (underline(_))
    Isso é um consenso comum entre programadores de Python
    Basicamente o (underline(_)), serve para dizer que ali é uma variável que não é utilizada
'''