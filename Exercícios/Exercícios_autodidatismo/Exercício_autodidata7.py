'''
Repetir uma palavra
Peça uma palavra e um número, e mostre a palavra repetida aquela quantidade de vezes.
'''

palavra = input('Digite a palavra que você deseja repetir: ')
repetir = input('Digite quantas vezes você deseja repetir: ')

rep_int = int(repetir)

repeticao = 1
while repeticao <= rep_int:
    
    print (palavra)
    repeticao += 1

# Facil pra carai