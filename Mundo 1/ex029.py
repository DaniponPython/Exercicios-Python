"""
29 - Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma msg dizendo que ele foi multado.
A multa vai custar R$ 7.00 por cada km acima do limite
"""
velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de '
          '80 km/h\033[m')
    print(f'\033[31mVocẽ deverá pagar uma multa de R$ \033[1m'
          f'{(velocidade - 80) * 7:.2f}\033[m')
print('\033[33mTenha um bom dia! Dirija com cuidado!\033[m')
