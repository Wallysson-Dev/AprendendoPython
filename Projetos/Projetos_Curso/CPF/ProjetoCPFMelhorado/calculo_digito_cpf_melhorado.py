import random
import sys

def gerar_cpf():
    cpf_gerado = []
    for _ in range(9):
        cpf_gerado += str(random.randint(0, 9))
    return (cpf_gerado)

def primeiro_digito():
    soma = 0
    multiplicacao = 10

    cpf_gerado = gerar_cpf()

    for numero in cpf_gerado:
        soma += int(numero) * multiplicacao
        multiplicacao -= 1

    divisao = (soma * 10) % 11
    verificacao = 0 if divisao > 9 else divisao

    cpf_gerado.append(str(verificacao))

    return(cpf_gerado)

def segundo_digito():
    soma = 0
    multiplicacao = 11
    for numero in cpf_gerado:
        soma += int(numero) * multiplicacao
        multiplicacao -= 1

    divisao = (soma * 10) % 11
    verificacao = 0 if divisao > 9 else divisao
    
    cpf_gerado.append(str(verificacao))

    return(cpf_gerado)

def formatacao_cpf():
    cpf_formatado = cpf_gerado
    cpf_formatado = "".join(str(cada_numero) for cada_numero in cpf_gerado)

    cpf_pronto = (
        f"{cpf_formatado[:3]}."
        f"{cpf_formatado[3:6]}."
        f"{cpf_formatado[6:9]}-"
        f"{cpf_formatado[9:]}"
    )
    return (cpf_pronto)

for _ in range(1):
    # Calcula o 1º dígito
    cpf_gerado = primeiro_digito()

    # Calcula o 2º dígito
    cpf_gerado = segundo_digito()

    # Mostra o CPF pronto
    cpf_pronto = formatacao_cpf()
    print(cpf_pronto)