# Formatação de string usando format

a = 'A'
b = 'B'
c = 1.1
formato1 = 'a={0} b={1} c={2:.2f}'.format(a, b, c)# Desde que a ordem esteja predefinida, a repetição é 'ativada'
# A quantidade de chaves, deve ser a mesma quantidade que entra no '.format', (se a ordem não estiver predefinida)

# O .format, só funciona se estiver seguindo de uma string
# O que fica dentro do .format, é chamado de argumento
# Existe uma coisa chamada de parametro nomeado
#  (n1=a, n2=b, n3=c)
# O parâmetro nomeado, normalmente, se utiliza para facilitar predefinir a ordem que vai ser executada
# Exemplo:
# A ordem no python, sempre começa do zero (0)
# formato = 'c={2} a={0} b={1:.2f}'.format(n1=a, n2=b, n3=c) # Nesse caso, iria apresentar um erro, já que a ordem está 'bagunçada', o certo seria (0, 1, 2)
# Porém caso e use o parâmetro nomeado:
formato2 = 'c={n3} a={n1} b={n2}'.format(n1=a, n2=b, n3=c)# Aqui deu certo por ter os parâmetros nomeados e dentro do .format
# Tanto faz a ordem, e a repetição é permitida
formato3 = 'c={n3} c={n3} c={n3} a={n1} b={n2}'.format(n1=a, n2=b, n3=c)
print(formato1)
print(formato2)
print(formato3)