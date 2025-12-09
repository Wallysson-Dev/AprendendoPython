# Operadores 'in' e 'not in'
# Strings são iteráveis("""navegáveis""")
# in e not in, simplificando, "in" significa 'está entre', e "not in" significa 'não está entre'
# São bool(boolean), ou seja, checa se tem determinada coisa e mostra se tem(True) ou se não tem(False)

#  0 -  1 -  2  - 3  - 4 - 5
#  O -  T -  Á  -  V - I - O
# -6 / -5 / -4 / -3 / -2 / -1

nome = 'OTÁVIO'
print (nome [2]) # Irá mostrar a letra de acordo com o número, nesse caso é 'Á'
print (nome [-2]) # Irá mostrar a letra de acordo com o número, nesse caso é 'I'

print ('O' in nome) # Verifica se tem 'O', no caso é True, já que 'O', tem no nome 'OTÁVIO'
print ('Z' in nome) # Verifica se tem 'Z', no caso é False, já que 'Z', não tem no nome 'OTÁVIO'

# Not in é a mesma coisa que in, porém invertido
print ('Z' not in nome) # Verifica se tem 'Z', no caso é True, já que 'Z', não tem no nome 'OTÁVIO'
print ('T' not in nome) # Verifica se tem 'T', no caso é False, já que 'T', não tem no nome 'OTÁVIO'

# Brincadeiras usando in

nome = input ('Digite seu nome: ')
encontrar = input ('O que você quer encontrar?: ')

if encontrar in nome:
    print (f'{encontrar} está entre {nome}')
elif encontrar not in nome:
    print (f'{encontrar} não está entre {nome}')