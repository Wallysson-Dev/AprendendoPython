# Exercício de Lógica – Contar vogais

# Ler a palavra
# Criar um contador e adicionar mais 1, caso seja uma vogal (a, e, i, o, u)
# Iterar a palavra e verificar se a letra é igual a 'range' de letras(vogais)
# Mostrar a quantidade de vogais na palavra lida

palavra = input('Digite uma palavra: ').lower()
contador = 0
vogais = ('a', 'e', 'i', 'o', 'u')
i = 0

while i < len(palavra):

    if palavra[i] in vogais:
        contador += 1

    i += 1

print(contador)

# Usei if palavra[i] == vogais: e isso estava errado porque eu tentava comparar uma letra com todas as vogais ao mesmo tempo.
# O correto é if palavra[i] in vogais:, pois o in verifica se a letra está dentro da variável vogais.