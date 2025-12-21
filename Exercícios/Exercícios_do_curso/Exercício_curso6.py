'''
1º Usar o while para 'passar' dentro de cada 'casinha' de uma str

2º Usar um while para por um '*' entre cada letra da str
'''

# 1º

nome = 'João Frajolinha'
contado = len(nome)

indice = 0
while indice < contado:
     print (nome[indice])
     indice += 1


# 2º 

nome = 'José galinasseo'
contado = len(nome)

indice = 0
novo_nome = ''
while indice < contado:
    letra = nome[indice]
    novo_nome += (f'*{letra}')
    indice += 1

novo_nome += '*'
print (novo_nome)