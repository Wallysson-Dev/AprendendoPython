'''
Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno.
A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5.
Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.
'''

nota_a = float(input('Digite a primeira nota: '))
nota_b = float(input('Digite a segunda nota: '))
nota_c = float(input('Digite a terceira nota: '))

peso_a = 2
peso_b = 3
peso_c = 5

resposta = ((nota_a * peso_a) + (nota_b * peso_b) + (nota_c * peso_c)) / (peso_a + peso_b + peso_c)

print(f'Sua média foi de {resposta:.2f} pontos')