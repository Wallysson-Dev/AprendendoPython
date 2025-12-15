'''
Exercício — Somar números até o usuário parar

Peça para o usuário digitar números repetidamente.
Use while para continuar perguntando até ele digitar 0.
'''

escolha1 = input ('Digite o primeiro valor: ')
numero = 0
intescolha1 = int(escolha1)
numero = intescolha1

while True:
    escolha2 = input ('Digite outro valor: ')
    intescolha2 = int (escolha2)
    numero = numero + intescolha2
    print (numero)
    if intescolha2 == 0:
        print ('Acabou')
        break
