# Operadores lógicos
# and (e), or (ou), not(não), None (não valor/não existe)

# and - Todas condições precisam ser verdadeiras
# Caso não seja, irá considerar tudo falso, e retornar o valor do false

# 1- :D  2- :(  \ :(
# 1- :D  2- :D  \ :)

# Se os dois ficarem felizem, eu estarei feliz
# Se um estiver triste, eu ficarei triste

# Or
# Se um estiver verdadeiro, tudo sera verdadeiro

# 1- :D 2- :(  \ :)
# 1- :( 2- :(  \ :(

# Se um estiver feliz, eu estarei feliz
# Se os dois estiver triste, eu estarei triste

# entrada = input ('Entrar ou Sair? :')
# senha_dg = input ('Senha: ')
# senha_c = '123'

# if (entrada == 'Entrar' or entrada == 'entrar') and senha_dg == senha_c:
    # O que está entre parenteses, ele avalia como um inteiro
    # Caso um estiver certo, irá ser true
#    print ('Entrou')
# else:
#     print ('Saiu')

# Avaliação de curto circuito

# print (True and True and True)
# print (True and 0 and True)

# Ele para de executar se identificar um false e retorna o false
# Falsy conhecidos até o momento (0, 0.0, '' false)

print (0 or False or 'abc' or 10 == 10)
# O 'or', avalia todas e retorna o true
# Ele para de avaliar, assim que identificar um true

senha = input('Senha: ') or 'Sem senha'
print (senha)
# Assim é como se fosse um if, pois caso o usuário não digite nada, a outra str, se torna true