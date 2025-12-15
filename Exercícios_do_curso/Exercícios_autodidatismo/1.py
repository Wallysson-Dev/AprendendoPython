# Verificar se o usuário é de maior

idade_usuario = input('Idade: ')
maioridade = 18

try:
    idade = int(idade_usuario)
    if idade >= maioridade:
        print ('Maior')
    else:
        print ('Menor')
except:
    print ('N é um número')


# Tava errando a questão da coersão, o int não pode ficar sozinho, ele eve ser atribuido a uma variavel.
# Exemplo

'''
Errado:
   int(idade_usuario) 

Certo:
    idade = int(idade_usuario)
'''