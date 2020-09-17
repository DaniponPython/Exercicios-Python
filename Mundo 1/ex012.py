"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5%
de desconto
"""

preco = float(input('Qual é o preço do produto? R$ '))
print(f'O produto que custava \033[34mR$ {preco:.2f}\033[m, na '
      f'promoção com desconto de \033[31m5%\033[m vai custar R$'
      f' \033[34m{preco * .95:.2f}\033[m.')