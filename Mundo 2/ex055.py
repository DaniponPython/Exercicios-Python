"""
Faça um programa que leia o peso de 5 pessoas e no final mostre qual foi o
maior e qual foi o menor peso lidos.
"""
maior = menor = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior:.1f} kg\n'
      f'O menor peso lido foi de {menor:.1f} kg.')
