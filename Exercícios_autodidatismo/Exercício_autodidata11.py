'''
Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno.
A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5
(A soma dos pesos portanto é 11). Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.
'''

nota_a = float(input('Digite a primeira nota: '))
nota_b = float(input('Digite a segunda nota: '))

peso_a = 3.5
peso_b = 7.5

mult_a = (nota_a * peso_a) + (nota_b * peso_b)
resposta = mult_a / (peso_a + peso_b)

print(f'Sua média foi de {resposta:.2f} pontos')