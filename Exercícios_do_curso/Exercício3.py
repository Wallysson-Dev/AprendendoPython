# Coletar dois valores e fazer aparecer o maior primeiro

valor1 = int(input ('Digite o primeiro valor: '))
valor2 = int(input ('Digite o segundo valor: '))

if valor1 > valor2:
    print(f'O valor {valor1} é maior que o valor {valor2}')
elif valor2 > valor1:
    print (f'O valor {valor2} é maior que o valor {valor1}')
else:
    print (f'O valor {valor1} e o valor {valor2}, são iguais')