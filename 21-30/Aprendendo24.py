"""
Fatiamento de string

 012345678
 OLÁ MUNDO
-987654321

A função len, conta quantos caracteres tem

Fatiamento [inicio:final:passo]
passo = pula de acordo com o número, o padrão é 1

"""

# Para fatiar

variavel = 'Olá mundo'
print(variavel [3:])
# Caso o final fique vazio, irá ler até o fim da str

print (variavel[3:6])
# A letra final não irá aparecer, então deve ser colocado um número a mais

print (variavel [::2])# -> Aqui irá pular 2 casa
# Irá mostrar (O)l(á) (m)u(n)d(o)

# Para inverter
print (variavel [::-1])
# Caso queira definir inicio e final, deve se utilizar número negativos
print (variavel [-3:-10:-1])