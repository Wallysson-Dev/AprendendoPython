# Operados lógico "not"
# É usado para inverter expressões

# not True = False
# not False = True

senha = input ('Senha: ')
if not senha == '123':
    print ('Você não digitou nada')

# Nesse caso, a str vazia ou com a senha errada, se torna false, porém o 'not' inverte, se tornando true e executando o código if
# O if só executa se for True