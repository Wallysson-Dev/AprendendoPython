'''
Segundo desafio, fazer um calculador de imc, com os dados definidos
'''

nome = 'Wallysson Davi'
peso = 87
altura = 1.84
# imc = ... # Ellipsis(...), serve pra dizer que depois o código será escrito
imc = peso / (altura * altura)

# Como eu fiz
print(nome)
print (str(peso) + 'kg')
print (str(altura) + 'cm')
print (imc)

# Como o professor fez
print (nome, 'tem', altura, 'cm')
print ('Pesa', peso, 'kg')
print ('E seu imc é:', imc)