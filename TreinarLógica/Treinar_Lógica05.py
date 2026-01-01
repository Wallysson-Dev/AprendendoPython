'''
Exercício 1 — Desconto

Crie uma função que:
Receba preco
Se o preço for maior que 100, aplique 10% de desconto
Caso contrário, mantenha o preço
Retorne o preço final

Use operação ternária
'''


# def calcular_desconto():
#     preco = float(input('Qual o valor do produto?: '))
#     desconto =  preco - (preco / 10)
#     verificacao = desconto if preco > 100 else preco
#     return verificacao

# print(calcular_desconto())


'''
Exercício 2 — Login simples

Crie uma função que:
Receba usuario e senha

Retorne: "Acesso permitido" se:
usuário == "admin" e
senha == "123"
Caso contrário, "Acesso negado"

Use operação ternária
'''


# def liberacao():
#     cargo = input('Digite seu cargo: ').lower().strip()
#     senha = input('Digite sua senha: ').strip()
#     verificacao = 'Acesso permitido' if cargo == 'admin' and senha == '12309' else 'Acesso negado'
#     return verificacao
# print(liberacao())


'''
Exercício 12 — Classificação de nota

Crie uma função que:
Receba uma nota de 0 a 10

Retorne:
"Excelente" se nota ≥ 9
"Bom" se nota ≥ 7
"Regular" se nota ≥ 5
"Insuficiente" caso contrário

Use operação ternária encadeada
'''


# def classificar_nota(nota):
#     classificacao = 'Excelente' if nota >= 9 else 'Bom' if nota >= 7 else 'Regular' if nota >= 5 else 'Insuficiente'
#     return classificacao
# print(classificar_nota(int(input('Digite sua nota: '))))


'''
Exercício 3 — Ano bissexto

Crie uma função que:
Retorne "Bissexto" se:
O ano for divisível por 4 e
Não for divisível por 100
ou
For divisível por 400
Caso contrário, "Não bissexto"

Use operação ternária
'''


# def ano_bissexto(ano):
#     calculo_bissexto = ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)
#     resultado = 'Bissexto' if calculo_bissexto else 'Não bissexto'
#     return resultado
# print(ano_bissexto(int(input('Ano: '))))