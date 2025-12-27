'''
Enumarate - É uma funcão(enumerate(x)) que enumera valores de iteráveis

lista = ['Maria', 'João', 'Joelma']
lista_enumerada = enumerate(lista)
    Caso dê print nessa variável, irá mostrar em qual local da memória foi armazenado

Para exibir a lista enumerada, devemos usar for, que pode ser usado dentro de while
    Exemplo:
        lista = ['Maria', 'João', 'Joelma']
        while True:
            lista_enumerada = enumerate(lista)
            for item in lista_enumerada:
                print(item)
            break
    Ou usamos somente for:
        lista = ['Maria', 'João', 'Joelma']
        lista_enumerada = enumerate(lista)
        for item in lista_enumerada:
            print(item)
Dos dois jeitos, irá exibir várias tuplas

O diferencial do enumerate, é que ele 'zera', caso ele for executado uma vez, ele para de ser executado
É como se o que estava dentro dele, tivesse sido 'comido'

Para contornar isso de 'esgotar', 'zerar' o enumerate é simples, basta colocar ele na função, ao invés de fora dela
    Devemos fazer assim:
        lista = ['Maria', 'João', 'Joelma']
        for item in enumerate(lista):
            print(item)
    Assim ele sempre vai voltar, caso precise ser usado de novo

O enumerate, podemos falar da onde ele vai começar a 'contar'
    utilizamos o 'start = x'
    Exemplo:
        lista = [1, 2, 3]
        lista_enumerada = enumerate(lista, start = 10)
        print(lista_enumerada)

        Irá mostrar:
            (10, 1)
            (11, 2)
            (12, 3)


            
*Para evitar mais linhas no código*
Existe uma boa prática de programação que evita linhas, sendo ela:
    lista = ['Maria', 'João', 'Helena']
    for indice, nome in enumerate(lista):
        print(indice, nome)
    Desse jeito, o for ja separa automaticamente

Geralmente as pessoas fazem assim:
    lista = ['Maria', 'João', 'Helena']
    for item in enumerate(lista):
        indice, nome = item
        print(indice, nome)
    Desse jeito, você separa manualmente, e ainda aumenta o código, é algo desnecessário

'\t - é como se fosse um tab'
f'\t{variável}'
'''