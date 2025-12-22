import os
import sys

nome_usuario = input("Digite o seu nome: ")
print(f"Olá {nome_usuario}!")
tamanho_acai = input(
    "Digite o tamanho do seu açaí: [A] 300ml, [B] 500ml, [C] 750ml, [S] Sair: "
).lower()
ingredientes_disponiveis = [
    "Granola",
    "Leite condensando",
    "Leite ninho",
    "Ovomaltine",
    "Morango",
    "Banana",
    "Nutella",
]
ingredientes_escolhidos = []
contador_escolhas_disponiveis = 3
preco_a, preco_b, preco_c = "R$19,00", "R$ 24,00", "R$47,50"

if tamanho_acai == "a":
    os.system("cls")
    print("Opção [A] 300ml selecionada com sucesso!")

    while len(ingredientes_escolhidos) < 3:
        print(ingredientes_disponiveis)
        print(f"Você pode escolher mais {3 - len(ingredientes_escolhidos)}")
        escolha_ingredientes = input("Escolha um ingredientes: ").capitalize()
        if escolha_ingredientes not in ingredientes_disponiveis:
            print("Escolha ingredientes disponiveis na lista por favor")
            continue
        ingredientes_escolhidos.append(escolha_ingredientes)
    os.system("cls")
    print(f"Você escolheu {ingredientes_escolhidos}")
    print(f"Você deve pagar {preco_a}")
elif tamanho_acai == "b":
    os.system("cls")
    print("Opção [B] 500ml selecionada com sucesso!")

    while len(ingredientes_escolhidos) < 3:
        print(ingredientes_disponiveis)
        print(f"Você pode escolher mais {3 - len(ingredientes_escolhidos)}")
        escolha_ingredientes = input("Escolha um ingredientes: ").capitalize()
        if escolha_ingredientes not in ingredientes_disponiveis:
            print("Escolha ingredientes disponiveis na lista por favor")
            continue
        ingredientes_escolhidos.append(escolha_ingredientes)
    os.system("cls")
    print(f"Você escolheu {ingredientes_escolhidos}")
    print(f"Você deve pagar {preco_b}")

elif tamanho_acai == "c":
    os.system("cls")
    print("Opção [C] 750ml selecionada com sucesso!")

    while len(ingredientes_escolhidos) < 3:
        print(ingredientes_disponiveis)
        print(f"Você pode escolher mais {3 - len(ingredientes_escolhidos)}")
        escolha_ingredientes = input("Escolha um ingredientes: ").capitalize()
        if escolha_ingredientes not in ingredientes_disponiveis:
            print("Escolha ingredientes disponiveis na lista por favor")
            continue
        ingredientes_escolhidos.append(escolha_ingredientes)
    os.system("cls")
    print(f"Você escolheu {ingredientes_escolhidos}")
    print(f"Você deve pagar {preco_c}")

elif tamanho_acai == "s":
    print(f"Tchau {nome_usuario}!")
    sys.exit()
else:
    print("Digite escolhas possíveis por favor")



# ----------------- RESUMO (ERROS E APRENDIZADO) -----------------
#
# Principais dificuldades:
# - Usei o os.system("cls") no lugar errado, o que fazia mensagens
#   sumirem da tela.
# - Tive dificuldade em controlar o fluxo do while, permitindo
#   escolhas além do limite esperado.
# - A validação de texto falhava por causa de letras maiúsculas
#   e minúsculas, resolvido com o uso do .capitalize().
# - No início, o usuário conseguia escolher ingredientes inválidos
#   por falta de verificação adequada.
#
# O que aprendi:
# - A ordem das instruções influencia diretamente o que o usuário vê.
# - Validar entrada do usuário é essencial para evitar erros.
# - Padronizar entradas de texto evita problemas de comparação.
#
# Conclusão:
# Este projeto ajudou a fortalecer minha lógica de programação,
# especialmente controle de fluxo, validações e interação com o usuário.
# Os erros fizeram parte do processo e ajudaram no entendimento do código.
#
# Feedbacks são bem-vindos :)
# ---------------------------------------------------------------