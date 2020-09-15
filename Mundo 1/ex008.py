"""
Escreva um programa que leia um valor em metros e o exiba convertido em cm e mm
"""
dist = float(input('Uma distância em metros: '))
print('\033[33m=*=\033[m'*11)
print(f'A medida de {dist}m corresponde a:')
print('\033[33m=*=\033[m'*11)
print(f'\033[36m{dist/1000:.2f} km\033[m')
print(f'\033[36m{dist/100:.2f} hm\033[m')
print(f'\033[36m{dist/10:.2f} dam\033[m')
print(f'\033[35m{dist*10:.2f} dm\033[m')
print(f'\033[35m{dist*100:.2f} cm\033[m')
print(f'\033[35m{dist*1000:.2f} mm\033[m')
