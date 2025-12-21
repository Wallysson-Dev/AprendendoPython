'''
List - Python

list vazia ([]) é considerada false
A list suporta vários valores de qualquer tipo. Inclusive outra list '[1, 2, [3, 4]]'

list pode ser acessado por índice
list é mutável, pode ser reescrito, exemplo:
    lista = ['Luiz']
    lista[0] = 'ABC'
    lista passa a ser:
        ['ABCuiz']

listas caso forem muito grandes, consomem muito processamento, deixando o código lento
pois o python reorganiza automaticamente, exemplo:
            0    1   2   3   4
    lista = [10, 20, 30, 40, 50]
    del lista[2]
    lista passa a ser:
         0   1   2   3
        [10, 20, 40, 50]
    Se a lista for muito grande, essa reorganização pode deixar o código lento
    Por isso para evitar problemas, é bom retirar ou adicionar do final da lista

Métodos Úteis-

.append() - adiciona algo no final da lista
    lista = [10, 20, 30]
    lista.append(1) -> Dentro do parenteses, coloca oq vai ser adicionado
    lista passa a ser:
        [10, 20, 30, 1]

.pop() - remove item da lista
    lista = [10, 20, 30]
    lista.pop() -> caso o parentese estaja vazio, o python considera o ultimo numero
    lista passa a ser:
        [10, 20]

.pop() - retorna o valor removido
    lista = [10,20, 30]
    print (lista.pop())
    Irá mostrar '30'

.pop() -> dentro do parenteses pode usar indice
             0   1   2   3
    lista = [10, 20, 30, 40]
    lista.pop(2)
    lista passa a ser:
        [10, 20, 40]

del - funciona igual o pop, mas ele não retorna nada
Não é aceito dentro do print

clear - Limpa a lista
    lista = [10,20, 30]
    lista.clear() -> Não pode por nada no parenteses, gera erro
    lista passa a ser vazia

.insert() - Adiciona um item no indice escolhido
    lista.insert(x, Y)
        x- indice que irá ser adicionado
        Y- item que vai ser adicionado
    
             0   1   2
    lista = [10, 20, 30]
    lista.insert (0, 5)
    lista passa a ser:
         0  1   2   3
        [5, 10, 20, 30]

.extend() - Adiciona vários itens de uma vez em uma lista existente
'Como se fosse um balde que despeja em outro balde'
    lista1 = [10, 20, 30]
    lista2 = [40, 50, 60]
    lista1.extend(lista2)
    lista passa a ser:
        [10, 20, 30, 40, 50, 60]
    
    Ele pega todos itens da lista2 e, adiciona dentro da lista1

(+ ou -) - concatena a lista
    lista1 = [10, 20, 30]
    lista2 = [40, 50]
    lista3 = lista1 + lista2
    lista passa a ser:
        [10, 20, 30, 40, 50]

Pode parecer a mesma coisa que o .extend(), porém usando (+ ou -), eu devo criar outra lista
'''