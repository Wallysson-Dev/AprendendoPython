"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'uzumaki'
tentativas = 0
letra_acertada = ''
letra_errada = ''

while True: 

    letra_usuario = input ('Digite uma letra: ')

    if len(letra_usuario) > 1:
        print('Digite apenas uma letra')
        tentativas += 1
        continue

    if letra_usuario in palavra_secreta:
        letra_acertada += letra_usuario
        tentativas += 1    
    else:
        letra_errada += letra_usuario
        print(letra_errada)
        tentativas += 1

    palavra_mostrada = ''
    for letra in palavra_secreta:
        if letra in letra_acertada:
            palavra_mostrada += letra
        else:
            palavra_mostrada += '*'
    print (palavra_mostrada)
    
    if palavra_mostrada == palavra_secreta:
        os.system('cls')
        print(f'Você venceu! Tentativas: {tentativas}')
        break