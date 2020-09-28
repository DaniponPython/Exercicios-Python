"""
31 - Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$ 0.50 por km para viagens de até 200km
e R$ 0.45 para viagens mais longas.
"""
distancia = int(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distancia} km')
if distancia < 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print(f'E o preço da sua passagem será de R$ {preco:.2f}')
