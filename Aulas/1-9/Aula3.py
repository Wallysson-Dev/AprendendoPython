'''
Python é uma linguagem dinâmica, ele consegue identificar se um número é inteiro ou real
Str -> string -> Texto
String são textos dentro das aspas 
'''

'''
As aspas não tem diferença pro python, tanto faz se for aspas duplas (""), ou aspas simples ('')
'''

print ('teste')# -> Vai exibir (teste)
print ('Teste \' escape')# -> Vai exibir (' escape) 
print (r'Teste \' escape\'')# -> Vai exibir (\' escape\')

# (\) Esse caractere é usado como escape, caso o (r) seja colocado antes das aspas, ele ira mostrar o caractere de escape
# Geralmente não se utiliza o (escape), ou o (r), Já que complica o codigo

# Normalmente se utiliza aspas duplas dentro das aspas simples, como o exemplo abaixo
print ('Testando "outro teste"')# -> Vai exibir(imprimir) "outro teste"
print ("Testando 'outro teste'")# -> Vai exibir(imprimir) 'outro teste'