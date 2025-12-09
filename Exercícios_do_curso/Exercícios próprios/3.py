# Verificar se uma palavra é palindromo (igual de tras pra frente)

palavra = input ('Qual a palavra?: ')

if palavra [::-1] == palavra:
    print (f'A palavra {palavra} é um palindromo')
else:
    print (f'A palavra {palavra} não é um palindromo')