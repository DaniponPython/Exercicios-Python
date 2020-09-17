"""
Escreva um programa que pergunte a quantidade de km percorridos por um carro
alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a
pagar, sabendo que o carro custa R$ 60.00 por dia e R$ 0.15 por km rodado
"""
dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos km rodados? '))
print('\033[1mO total a pagar é de '
      f'\033[36mR$ {dias * 60 + km * .15:.2f}\033[m')