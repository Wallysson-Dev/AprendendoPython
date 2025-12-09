# Coersão é o ato de mudar um tipo pra outro tipo
# Existem vários nomes, os mais comuns são:
# Conversão de tipos, Type convertion, Type casting, coercion
# Tipos imutavéis e primitivos:
# str, int, float e bool <- esses são os tipos que eu conheço até o momento
# Concatenar (concatenate), significa "juntar/somar"

print(int('10'), type(int('10')))# -> O código executa de dentro pra fora "(3º(2º(1º)2º)3º)"
print(str(12) + "A")# -> Transforma o 'int' em 'str'
print (bool('  '))# -> Por não ter nada, ele mostra que é verdadeiro
print (float("10") + 4)# -> Por ser do tipo 'float', ele adiciona uma casa decinal no número