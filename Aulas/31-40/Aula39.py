'''
Imprecisão de Ponto fltuante(float)

n1 = 0.1
n2 = 0.7
n3 = Deveria ser 0.8
Mas o computador mosta 0.799999

Normalmente formatando o código ja resolve
n1 = 0.1
n2 = 0.7
n3 = n1 + n2
print(f'{n3:.2f})

Caso não possamos formatar o código
Exite 2 jeitos de resolver esse problema

Jeito 1 - utilizando 'round()'

print(round(n3, x))
               'x' = números de casas decimais
               Não são preenchidos com zeros, são preenchidos com espaços

Jeito 2 - decimal.Decimal

import decimal

n1 = decimal.Decimal (0.1)
n2 = decimal.Decimal (0.7)
Caso seja passado como int, o decimal, vai calcular todo número, nesse caso iria mostrar:
    n3 = 0.7999...611421941381
Esse jeito é utilizado em calculadoras muito precisas

Então para resolver o erro inicial, devemos passar o tipo str dentro do decimal, assim ele corrige a lógica automaticamente

import decimal

n1 = decimal.Decimal ('0.1')
n2 = decimal.Decimal ('0.7')
n3 = n1 + n2
Agora o n3 representa 0.8

'''