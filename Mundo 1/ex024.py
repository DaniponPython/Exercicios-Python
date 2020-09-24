"""24 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou
não com a palavra "SANTO".
"""

city = input('Digite o nome da sua cidade: ').strip().title()
div = city.split()
print(f'Sua cidade começa com "Santo"? {"Santo" in city}')
