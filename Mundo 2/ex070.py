"""
Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar. No final, mostre:
a) Qual é o total gasto na compra
b) Quantos produtos custam mais de R$ 1000,00
c) Qual é o nome do produto mais barato
"""
print('~' * 30)
print('      LOJA SUPER BARATAO')
print('~' * 30)

nome_barato = ''
preco_barato = total = mais_1000 = c = 0
while True:
    c += 1
    nome = input('Nome do produto: ')
    preco = float(input('Preço: R$ '))
    total += preco

    if c == 1 or preco < preco_barato:
        nome_barato = nome
        preco_barato = preco

    if preco > 1000:
        mais_1000 += 1
    resp = ' '
    while resp not in'SN':
        resp = input('Quer continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}\n'
      f'Temos {mais_1000} produto(s) custando mais de R$ 1.000,00\n'
      f'O produto mais barato foi {nome_barato} e custa R${preco_barato:.2f}')
