"""
Calculadora While
"""

# A função .lower() transforma a string em minúsculas
# A função .startswith() verifica se a string começa com o caractere especificado dentro dos parênteses

while True:

    numero_1 = input("Digite um valor: ")
    numero_2 = input("Digite outro valor: ")
    operadores = input("Digite um operador (+-/*): ")

    numeros_validos = None

    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Digite números válidos")
        continue

    operadores_permitidos = "+", "-", "/", "*"

    if operadores not in operadores_permitidos:
        print("Digite operadores válidos")
        continue

    elif len(operadores) > 1:
        print("Digite apenas um operador")
        continue

    print("-" * 30)
    print("O Resultado irá aparecer logo abaixo")
    print("-" * 30)

    if operadores == "+":
        print(f"A soma do {numero_1} + {numero_2} = {num_1_float + num_2_float}")

    elif operadores == "-":
        print(f"A subtração do {numero_1} - {numero_2} = {num_1_float - num_2_float}")

    elif operadores == "*":
        print(
            f"A multiplicação do {numero_1} * {numero_2} = {num_1_float * num_2_float}"
        )

    elif (
        operadores == "/" and num_2_float == 0
    ):  # Aqui eu quebrei um pouco a cabeça, explicação no final do código
        print("O número zero, não pode ser dividido")
        continue

    elif operadores == "/":
        print(f"A divisão do {numero_1} / {numero_2} = {num_1_float / num_2_float}")

    sair = input("Deseja sair? (s/n): ").lower().startswith("s")

    if sair:
        print("Você saiu")
        break
    else:
        continue

"""
if operadores == '/' and num_2_float == 0:
        print ('O número zero, não pode ser dividido')
        continue
        
Traduzindo o que essa parte que eu nn estava entendendo

Se operadores for igual(==) a dividir('/') e o num_2_float for igual (==):
        print ('O número zero, não pode ser dividido')
        continue
        
Caso o usuario coloque zero no primeiro número, não irá gerar problemas, pq nenhum numero dividido/multiplicado por zero é zero


Eu estava fazendo assim:

if (operadores == '/') and (num_1_float == 0) or (num_2_float == 0):
        print ('O número zero, não pode ser dividido')
        continue
        
Desse jeito que eu tava fazendo, além de colocar caso o primeiro número seja zero, que não gera erro
O operador boolean and, 'junta' as duas coisas, exemplo:
    (operadores == '/') and (num_1_float == 0)
Desse jeito, o Python lê assim:
    (operadores == '/' and num_1_float == 0)
Assim, o lado (operadores == '/'), sempre será True, então o and irá parar de verificar, já que ele só verifica até encontrar um True
"""
