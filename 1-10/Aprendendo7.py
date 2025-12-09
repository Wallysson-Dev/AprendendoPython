# Variáveis é a famosa "etiqueta", que guarda na memória do computador
# Já aprendi isso nas aulas de algoritmo

# Para criar uma variável tem que seguir as 6 regrinhas:
# 1- Tem que iniciar com letra, porém o pep8, indica que a letra seja mínuscula
# 2- O resto pode ser letras ou números
# 3- Não utilizar nenhum símbolo, exceto (_)
# 4- Não pode ter espaços, é substituido por (_)
# 5- Não pode ter acentos
# 6- Não pode ser uma palavra já reservada

# O sinal de (=), é usado para colocar algo dentro da variável, exemplo:
data_de_nascimento = '10/12/2008' # -> Toda vez que data_de_nascimento, for utilizada, irá mostrar 10/12/2008.
print (data_de_nascimento) # -> Irá mostrar o que está dentro da variável

# Pode-se passar qualquer tipo pra uma variável
soma = 10 + 240
print(soma) # -> Irá exibir a soma das expressões, no caso 250

# A variável é muito utilizada, para que não precise escrever toda a funcão, exemplo:
i_1 = int ('1')
print (i_1, type('i_1'))# -> código usando variável
print(int('10'), type(int('10')))# -> código sem usar variável
# Assim facilita caso precise mudar algo numa repetição, ao invés de mudar um por um, com a variável, é apenas mudar o valor da variável
# Ser descritivel na variável, para facilitar a leitura
int_0 = bool('1')# -> Fazer assim, pode gerar confusão, já que a variável da a entender que seja int, porém ela é bool

nome = 'cleber'
idade = '18'
maior_de_idade = '18'
print (maior_de_idade <= idade)