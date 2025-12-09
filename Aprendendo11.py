# Introdução f-string (formatação de string)
# Serve pra facilitar a escritura do código, ao invés de ficar colocando vírgula e aspas ou usar concatenação dentro do print, usa-se o 'f', antes de uma variável, exemplo:

# Existe dois jeitos de ser realizado

nome = 'Wallysson Davi'
altura = 1.80
peso = 87

# Primeiro jeito
linha_1 = f'{nome} tem {altura} cm'# Tem que transformar tudo em str, o que tiver variável, eu uso '{}'
print (nome, 'tem', altura, 'cm')

# Segundo jeito
print (f'{nome} tem {altura} cm')# A formatação ja é feita diretamente no print

# Para formatar(definir) quantas casa decimais eu quero que apareça, eu utilizo o "":.(quantas casa eu quero após o ponto)f", exemplo:
linha_2 = f'{nome} tem {altura:.2f} cm'# Assim irá mostrar 1.80, ao invés de 1.8
print(linha_2)

imc = peso / (altura * altura)
print (f'{imc:,.2f}')# Agora, mostra apenas duas casa decimais

# O ":.*f", também serve para definir pontuação em números grandes, exemplo:
reais = 100000.3
print (f'{reais:,.2f}')# Irá mostrar 100,00.00, como o programa é inglês, as métricas, também são de lá