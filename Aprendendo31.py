'''
while dentro de while
É como se fosse engrenagens
Exemplo:
'''

qtd_linha = 3
qtd_colunas = 3

linha = 1
while linha <= qtd_linha:
    coluna = 1
    while coluna <= qtd_colunas:
        print (f'{linha=} {coluna=}')
        coluna += 1
    linha += 1
'''
O while 'pequeno' == 'que está dentro', só para de executar, quando ele chegar no 'objetivo' dele, e por ter um 'linha += 1', do while grande no final, \
  ele volta a executar o while grande, até ele também alcançar o 'objetivo' dele.
Caso não tivesse o 'linha += 1' do while 'grande', isso iria se tornar um loop infinito, já que a variável linha nunca seria igual variável qtd_linha
'''