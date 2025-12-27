# Operações condicionais
#  if / elif      / else
#  se / se não se / se não
# Essa é a ordem, 1º if, 2º elif, 3º else
# Pode se usar if e else, o elif não é obrigatório
'''
entrada = input ('Você quer "entrar" ou "sair"? ')
print ('Você entrou no sistema')
print ('Você saiu do sistema')

Sem usar as operações condicionais, não tem jeito de "escolher" oq será executado
Nesse caso apresentado acima, o código irá mostrar os dois print's, independente da escolha do usuário
'''

entrada = input ('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print ('Você entrou no sistema')
elif entrada == 'sair': # Pode ser repetido várias vezes
    print ('Você saiu do sistema')
else: # else é sempre a última opção
    print('Você não digitou, nem "entrar" e nem "sair"')
# Tem que fazer a dentação para funcionar