'''
Formatação fstrings
    Preencher

 > - Esquerda
 < - Direita
 ^ - Centro

Para utilizar isso, usa-se ":X(><^)Y"
O X é representado pelo caractere que será preenchido
O Y representa, qual o tamanho limite para ser preenchido

Preencher pode ser chamado de "pad"
Serve para organizar melhor os textos
Exemplo:
'''

variavel = 'Olá'
print (f'{variavel:>10}')# Irá preencher até ter a quantidade definida de caracteres, nesse caso 10
# Irá mostrar "       Olá"
# Nesse exemplo o X não foi definido, então automaticamente, o python utiliza o espaço
# o Y foi definido como 10, então o python irá preencher até ter 10 "casas", \
#  nesse exemplo, a variavel tem 3 "casas", então o python irá por 7 "casas", pra completar 10 "casas"

print (f'{variavel:-^9}')
# Irá mostrar "---Olá---"
# O X foi definido com '-'
# O Y foi definido como 9
# O sinal '^' faz o possivel para deixar no centro, nesse caso o número era 9, tirando 3 da variavel, sobra 6 se dividir por 2, sobra 3. \
#  Então fica 3 em cafa lado
# Caso seja um número que não vai ficar perfeito, exemplo 10, o python vai deixar ele "torto", então caso queira que fique no meio, \ 
#  deve ser um nùmero que fique igual dos dois lados
