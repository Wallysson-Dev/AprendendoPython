'''
Documentação - Tipos built-in, tipos imutaveis e ações

Tipos imutaveis que vimos até agora: str, int, float e bool
Built-in: São coisas que ja vem com python, vem embutidos

Doc do python 3.14.0: https://docs.python.org/pt-br/3/library/stdtypes.html
É muito importante estar sempre atualizado sobre as mudanças da linguagem
'''

# O que é tipos imutaveis?
# São aqueles que não podem ser "mudados"
# Exemplo:

# v1 = 'Luiz'
# v1[3] = 'ABC'

# Nesse caso, o computador vai tentar mudar apenas a letra z, para ABC. Porém o tipo str, é imutavel, por isso, gera um erro
# Para mudar isso, deveria ser criado outra variavel
# O jeito certo caso eu queira imprimir 'LuiABC'
# Seria assim:

v1 = 'Luiz'
v2 = f'{v1[:3]}ABC'

print (v2)

'''
str, int, float, bool e entre outros, são objetos

Nos objetos existem ações, que no vs code, aparece caso escreva '.(ponto)'
No doc do python, mostra todas as ações e explica todas elas

Por isso devemos sempre estar atualizado, para caso adicionem uma ação nova, ou remova uma ação antiga
Existem ações que são exclusivas de algum objeto

Dentro do vs code, caso não queira abrir o doc e ir atrás da ação, basta escrever '.(ponto)', que irá aparecer as ações \
 e do lado, terá uma setinha escondida que ensina a usar a ação especifica
'''