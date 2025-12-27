'''
split, join e strip - Métodos úteis para str

.split() - Separa aonde tem espaços brancos, ou o que o programador filtra
exemplo split vazio:
    frase = 'Estou aprendendo bastante'
    frase_palavras = frase.split()
    print(frase_palavras)
        Mostra:
        ['Estou', 'aprendendo', 'bastante'] - Separa onde tem espaços brancos
exemplo split com filtro:
    frase = 'Olha, que interessante'
    frase_filtro = frase.split(',') - Vai filtrar todas str que for igual a ',', e separar numa lista
    print(frase_filtro)
        Mostra:
        ['Olha'#,# ' que interessante']
               #virgula da lista#
               o espaço no ' que interessante', continua, para remover é só adicionar ', ' no filtro

.strip() - Corta espaços no começo e no fim
.rstrip() - Corta espaços da direita(right)
.lstrip() - Corta espaços da esquerda(left)

.join() - Une strings
A estrutura é = variavel = 'separador'.join(iterável)

frase_unidas = '-'.join('abc')
print(frases_unidas)
Mostra:
a-b-c
O que vem antes do .join, é o que vai separar o iteravel
O iterável fica dentro dos parenteses

'''
