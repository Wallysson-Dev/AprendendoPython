# Converter metros para centímetros e milímetros

metros = input ('Quantos metros?: ')
metros_1 = int(metros)
centimetros = metros_1 * 100
milimetros = centimetros * 100

print (f'Os centimetros de {metros_1} são {centimetros:,.0f} cm')
print (f'Os milimetros de {metros_1} são {milimetros:,.0f} mm')