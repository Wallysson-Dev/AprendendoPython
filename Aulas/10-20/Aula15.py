# Operações condicionais regrinhas
#  if / elif      / else
#  se / se não se / se não

condicao = False

# if condicao:
#    print ('Este código é do if')
#  print ('Este código é do if')
# Assim da erro, pq a dentação ta errada

if condicao:
    print ('Este código é do if')
elif condicao: # Lembrando que elif pode ser repetido
    ... # Ellipsis, serve pra dizer que o código será escrito depois, ele não irá causar erros, pois o computador vai ignorar
elif condicao: # Lembrando que elif pode ser repetido
    ...   
else:
    print ('Este código é do else')
# O if é o único operador condicional, que pode ficar sozinho
# Para usar o elif ou o else, é preciso ter if, pois eles dependem do if

# elif condicao: # Caso executado sem o if, da erro de sintaxe
#    print ('Este código é do elif')
# Caso a ordem "if / elif / else" for seguida, o código da erro de sintaxe
# Dentro de cada "bloco", pode ter várias linhas