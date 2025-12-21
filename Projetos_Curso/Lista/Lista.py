"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""

import os

lista_n = []

while True:
    print("Olá usuário")
    print("Selecione uma opção")
    escolha_usuario = input("[I] Inserir, [A] Apagar, [L] Listar, [S] Sair: ").lower()

    if escolha_usuario == "l":
        os.system("cls")
        if lista_n == []:
            print("Lista Vazia")
        else:
            for indice, item in enumerate(lista_n):
                print(indice, item)
    elif escolha_usuario == "i":
        adicionar = input("Insira algo: ")
        lista_n.append(adicionar)
        os.system("cls")
        print("Item adicionado na lista com sucesso!")
    elif escolha_usuario == "a":
        if lista_n == []:
            print("Lista Vazia")
        else:
            os.system("cls")
            print("Itens da lista: ")
            for indice, item in enumerate(lista_n):
                print(indice, item)
            apagar = input("Digite o número que você quer apagar: ")
            if apagar.isdigit():
                verificacao = int(apagar)
                if verificacao < 0 or verificacao >= len(lista_n):
                    os.system("cls")
                    print("Digite índices válidos")
                else:
                    os.system("cls")
                    lista_n.pop(verificacao)
                    print("Item apagado com sucesso!")
            else:
                os.system("cls")
                print("Digite apenas números")
    elif escolha_usuario == "s":
        break
    else:
        os.system("cls")
        print("Por favor digite alguma escolha possível")
        continue




# ----------------- RESUMO DOS EXERCÍCIOS (APRENDIZADO) -----------------
#
# Erros que cometi:
# - Em alguns exercícios usei a condição errada, porque li o enunciado rápido.
# - Inicializei o maior número com 0, mas aprendi que o certo é usar o primeiro
#   valor da lista.
# - Em um exercício imprimi a variável errada por falta de atenção.
# - Errei a lógica em uma substituição de valores, trocando números errados.
# - Tive dificuldade em exercícios de verificação e aprendi que é melhor
#   decidir o resultado fora do for.
#
# Como posso melhorar:
# - Ler o exercício com mais calma.
# - Pensar no que o código precisa fazer antes de escrever.
# - Conferir as condições e variáveis antes de finalizar.
# - Continuar praticando exercícios de lógica.
#
# Conclusão:
# Hoje cometi erros, mas entendi todos eles.
# Cada erro me ajudou a melhorar minha lógica de programação.
#
# Feedbacks são bem-vindos :)
# ----------------------------------------------------------------------
