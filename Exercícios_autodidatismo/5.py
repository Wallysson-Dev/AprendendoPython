'''
Exercício — Verificação de senha (tentativas infinitas)

Crie um programa que peça uma senha ao usuário.
Enquanto a senha estiver errada, continue perguntando.

Quando ele digitar a senha correta, exiba:
"Acesso permitido"
'''

senha_permitida = input ('Qual é a sua senha?: ')

while True:
    tentativa = input ('Tente uma senha: ')
    
    if tentativa == senha_permitida:
        print ('Você acertou a senha!')
        break
    else:
        print ('Você errou a senha, tente novamente')