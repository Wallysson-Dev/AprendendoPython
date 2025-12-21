'''
Introdução try / except

try -> Tentar executar o código
except -> Quando occorre algum erro ao executar

except pode ser chamado de "exceção" ou exceptions

try e except, é como se fosse um if, porém ele não "para de executar/mostra o erro"
'''

# Exemplo de try e except:

n_str = input ('Vou dobrar o número digitado: ')# -> O número será str

try:# -> não precisa de condição
    print ('STR: ', n_str)
    n_float = float(n_str)
    print ('FLOAT: ', n_float)
    n_int = int(n_float)
    print ('INT: ', n_int)
    print (f'O dobro do número é {n_float * 2}')
except:# -> também não precisa de condição
    print ('Isso não é um número')

# Caso o código "capture" um erro no try, automaticamente o except será executado
# Caso uma letra ser digitada, ele não poderá ser transformado em float ou int, gerando um erro e, executando o except

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')

# O if, caso ocorra um erro, ele irá mostrar o erro, e parar a execução