'''
id = mostrar onde está na memória do computador
Flags, is, is not, None

Flags(bandeiras), normamelmente usada para ver se o código passou por ali
is, is not e None, são normalmente usado juntos
is é a mesma coisa que ==

As bandeiras podem ser utilizadas erradas, caso a variavel seja atribuida dentro de um bloco
pois assim, ficariamos dependentes de uma função ser executada
'''

# Jeito errado

# con = True

# if con:
#     passou_no_if = True
#     print('Qualquer coisa')
# else:
#     print('Não faça nada')

# print (passou_no_if)

# Assim, caso o if não for executado, a variavel "passou_no_if", ficará vazia, gerando um erro na ultima linha do código


# Jeito certo

con = False
passou_no_if = None # O None significa "sem valor"

if con:
    passou_no_if = True # Mudamos a variavel pra True
    print('Faça algo')
else:
    print ('Não faça nada')

# Verificar se passou pelo if ou não

# 1º jeito
# Pode usar dois if's, para fazer a verificação

# if passou_no_if is None: # Verifica se o valor de "passou_no_if" é None, caso seja, irá executar o if
    # print ('Não passou pelo if')

# if passou_no_if is not None: # Verifica se o valor de "passou_no_if" não é None, caso não seja, irá executar o if
        # print ('Passou pelo if')
    
# 2º jeito
# Ou usa o if e o else

if passou_no_if is None:
    print ('Não passou pelo if')
else:
    print ('Passou pelo if')