# continue
# é uma função que até o atual momento, é apenas para o while, igual a função break

# continue - pula uma repetição. Exemplo:

contador = 0

while contador < 100:
    contador += 1
    
    if contador >= 40 and contador <= 80:# Caso o código caia dentro do if, o loop irá executar o bloco do if, e voltar a fazer o loop de novo, por isso diz 'pular' um loop
        print('Não vou mostrar o', contador)
        continue # Indica para o python que pode continuar
    print (contador)