'''
Refazendo meu primeiro projeto
Pouco mais de 1 mês de diferença
Testar minha evolução
'''

import random
import os

print('-'*30)
print('Seja bem-vindo ao Quiz')
print('-'*30)

pontos = 0
contador_acertos = 0
contador_erros = 0

perguntas = [
    'Qual é o formato do salgadinho Doritos?: ',# 0
    'Qual animal representa o símbolo da paz?: ',# 1
    'Quantos lados tem um dado?: ',# 2
    'O vinho é feito com qual fruta?: ',# 3
    'O pão de queijo é um prato típico de qual estado brasileiro?: ',# 4
    'Quantos dias tem um ano bissexto?: ',# 5
    'Como se chama o processo de “alimentação” das plantas?: ',# 6
    'Qual é o nome do satélite natural da Terra?: ',# 7
    'Como é chamada a água em estado sólido?: ',# 8
    'Qual é o país mais populoso do mundo?: ',# 9
    'Qual personagem do folclore brasileiro tem os pés voltados para trás?: '# 10
]

respostas = [
    ['triangular', 'triângulo', 'triangulo'],# 0
    ['pomba', 'pomba branca'],# 1
    ['seis', 'seis lados'],# 2
    ['uva'],# 3
    ['minas gerais'],# 4
    ['trezentos e sessenta e seis', 'trezentos e sessenta e seis dias', '366', '366 dias'],# 5
    ['fotossíntese', 'fotossintese'],# 6
    ['lua'],# 7
    ['gelo'],# 8
    ['india', 'índia'],# 9
    ['curupira']# 10
]

contador_perguntas = 0
contador_limpeza = 0

while True:
    if len(perguntas) == 0:
        os.system('cls')
        print('Você respondeu todas perguntas')
        break

    i = random.randint(0, len(perguntas) -1)
    resposta_usuario = input(perguntas[i]).strip().lower()

    if resposta_usuario in respostas[i]:
        print('Você acertou')
        pontos += 1
        contador_acertos += 1
    else:
        print('Você errou')
        pontos -= 1
        contador_erros += 1
        if pontos < 0:
            print('Você perdeu o jogo, tente novamente')
            continue

    perguntas.pop(i)
    respostas.pop(i)
    contador_perguntas += 1
    
    contador_limpeza += 1
    if contador_limpeza % 6 == 0:
        usuario_limpar = input('Deseja limpar sua tela?: ').strip().lower()
        sim = ['s', 'sim']
        if usuario_limpar in sim:
            print('Limpando sua tela...')
            os.system('cls')
        else:
            continue

    if contador_perguntas % 3 == 0:
        continuar_ou_parar = input('Você deseja continuar jogando?(Sim/Não): ').strip().lower()
        continuar = ['s', 'sim']
        if continuar_ou_parar in continuar:
            continue
        else:
            print('Obrigado por jogar!')
            break

os.system('cls')
print('=' * 30)
print('Resultados do Jogo')
print('=' * 30)

print(f'Sua pontuação foi de {pontos} pontos!')
print('-' * 30)
print(f'Sua contagem de acertos foi de {contador_acertos} acertos!')
print('-' * 30)
print(f'Sua contagem de erros foi de {contador_erros} erros')
if contador_erros == 0:
    print('WoW, você não errou nada!')
elif contador_erros >= 1 and contador_erros <= 5:
    print('Você não errou quase nada')


'''
Resumo do projeto / aprendizado:

Esse projeto foi refeito pouco mais de 1 mês depois do primeiro, com o objetivo de
testar minha evolução em lógica de programação.

No início eu tinha dificuldades com:
# comparação de strings
# validação da entrada do usuário
# repetição de código
# controle do fluxo do programa

Durante esse tempo aprendi, pratiquei e utilizei:
# uso de listas para organizar perguntas e respostas
# uso de índices para manter pergunta e resposta corretas
# sorteio de perguntas de forma aleatória sem repetição
# normalização de input com strip() e lower()
# uso de contadores para acertos, erros e controle do jogo
# operador módulo (%) para executar ações a cada X perguntas
# melhor uso de break e continue

Cometi poucos erros no caminho,
consegui identificar e corrigir sem problemas durante o desenvolvimento.

Esse projeto mostra claramente minha evolução em relação à primeira versão.

Lembrando sempre, FeedBacks são sempre bem-vindos
'''