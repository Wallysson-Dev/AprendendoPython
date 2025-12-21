'''
Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).
'''

distancia_percorrida = float(input('Digite a distância percorrida: '))
gasolina_gasta = float(input('Digite o gasto de gasolina na distância percorrida: '))

media_de_consumo = distancia_percorrida / gasolina_gasta
print(f'A média de consumo do veículo foi de {media_de_consumo:,.3f}km/l')