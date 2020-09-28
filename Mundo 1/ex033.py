"""
Faça um programa que leia 3 números e mostre qual é o menor e qual é o maior.
"""
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))
menor = maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O menor valor digitado foi {menor}\n'
      f'O maior valor digitado foi {maior}')
