'''
Meu Primeiro Projeto
'Quiz'
Testar minhas habilidades de lógica de programação
'''
print('-'*30)
print('Bem vindo ao Quiz')
print('-'*30)

pontos = 0

# Pergunta 1
pergunta1 = input('Qual a capital do Brasil?: ').lower()

if pergunta1 == 'brasilia' or pergunta1 == 'brasília':
    print('Você acertou!')
    pontos += 1
else:
    print('Você errou')
    if pontos >= 1:
        print ('Você perdeu um ponto')
        pontos -= 1
print(f'Pontos: {pontos}')

# Pergunta 2
pergunta2 = int(input('Em qual ano o Brasil foi invadido pela Colônia Portuguesa?: '))
resposta2 = 1500

if pergunta2 == resposta2:
    print('Você acertou!')
    pontos += 1
else:
    print('Você errou')
    if pontos >= 1:
        print ('Você perdeu um ponto')
        pontos -= 1
print(f'Pontos: {pontos}')