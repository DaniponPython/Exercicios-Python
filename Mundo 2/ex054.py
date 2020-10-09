"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
Considere maioridade = 18 anos
"""
from datetime import date
ano_atual = date.today().year
maior = 0
for c in range(1, 8):
    ano = int(input(f'Ano em que a {c}ª pessoas nasceu: '))
    idade = ano_atual - ano
    if idade >= 18:
        maior += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade\n'
      f'E também tivemos {7 - maior} pessoas menores de idade.')
