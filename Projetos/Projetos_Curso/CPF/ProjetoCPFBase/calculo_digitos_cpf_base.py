"""
Calculo dos dígitos do CPF
Primeiro colete a soma dos 9 primeiros dígitos do CPF
Segundo multiplique o valor da soma
    No calculo do primeiro digito, multiplique por 10
    No calculo do segundo digito, multiplique por 11
Terceiro pegue o valor do resto da multiplicação por 11
Quarto Verifique o valor
    Se o resultado for maior que 9:
        resultado é 0
    contrário disso:
        resultado é o valor da conta
"""

# Pensamento antes de começar a fazer o código:
# 1 - Coletar os 9 primeiros números do cpf do usuário
# 2 - Fazer o calculo dos números
# Calcular o primeiro dígito, e adicionar no cpf enviado pelo usuário
# Calcular o segundo dígito, e adicionar no cpf que contém o primeiro dígito calculado
# 3 - Montar o cpf com as pontuações
# 4 - Verificar se o cpf é valido (Se o cpf contém 11 números ao todo)
# Caso sim, mostrar "cpf valido"
# Caso não, mostrar "cpf invalido"

# 1º Dígito
soma = 0
multiplicacao_primeiro_digito = 10

cpf_enviado_pelo_usuario = input("Digite os primeiros nove números do seu cpf: ")

cpf_sem_pontuacao = [int(n) for n in cpf_enviado_pelo_usuario if n.isdigit()]

for numero in cpf_sem_pontuacao:
    soma += numero * multiplicacao_primeiro_digito
    multiplicacao_primeiro_digito -= 1

divisao = (soma * 10) % 11
verificacao_primeiro_digito = 0 if divisao > 9 else divisao

cpf_sem_pontuacao.append(verificacao_primeiro_digito)


# 2º Dígito
soma = 0
multiplicacao_segundo_digito = 11

for numero in cpf_sem_pontuacao:
    soma += numero * multiplicacao_segundo_digito
    multiplicacao_segundo_digito -= 1

divisao = (soma * 10) % 11
verificacao_segundo_digito = 0 if divisao > 9 else divisao

cpf_sem_pontuacao.append(verificacao_segundo_digito)

cpf_formatado = "".join(str(cada_numero) for cada_numero in cpf_sem_pontuacao)

cpf_pronto = (
    f"{cpf_formatado[:3]}."
    f"{cpf_formatado[3:6]}."
    f"{cpf_formatado[6:9]}-"
    f"{cpf_formatado[9:]}"
)
print(cpf_pronto)
if len(cpf_sem_pontuacao) == 11:
    print("Seu CPF é válido")
else:
    print("Seu CPF não é válido")


# ----------------- RESUMO DO PROJETO (CÁLCULO DE CPF) -----------------
#
# Erros e dificuldades que enfrentei:
# - No início repeti muito código entre o cálculo do 1º e do 2º dígito.
# - Confundi a diferença entre modificar uma lista e atribuir o retorno
#   de métodos como append().
# - Precisei pensar melhor sobre quando converter dados para int ou str.
#
# Aprendizados principais:
# - Aprendi a limpar uma string mantendo apenas números.
# - Entendi melhor como funciona o cálculo dos dígitos verificadores do CPF.
# - Pratiquei o uso de operadores condicionais (if em uma linha).
# - Aprendi a transformar listas em strings formatadas com join() e f-strings.
#
# Como posso melhorar esse código no futuro:
# - Criar funções para evitar repetição de lógica.
# - Validar se o CPF digitado possui exatamente 9 números antes do cálculo.
# - Comparar os dígitos calculados com um CPF completo para validação real.
# - Sempre aprender como organizar melhor o código, para que fique mais claro.
#
# Conclusão:
# Este projeto representa um avanço importante no meu aprendizado em Python.
# Mesmo cometendo erros, consegui entender todos eles e corrigir a lógica.
# Cada dificuldade me ajudou a consolidar conceitos fundamentais de programação.
#
# Feedbacks e sugestões são bem-vindos :)
# ---------------------------------------------------------------------