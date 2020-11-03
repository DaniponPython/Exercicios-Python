"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
quantos dólares ela pode comprar
"""

n = float(input('Quanto dinheiro você tem na carteira? R$ '))
print(f'Com \033[31mR$ {n:.2f}\033[m você pode comprar \033[36mUS$ {n/4.11:.2f}\033[m')
