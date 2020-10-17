"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e quel foi o menor e qual foi o maior valor lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
c = soma = 0
resp = ''

while resp != 'N':
    num = int(input('Digite um número: '))
    c += 1
    soma += num

    if c == 1:
        maior = num
        menor = num

    if num > maior:
        maior = num

    if num < menor:
        menor = num

    resp = input('Quer continuar? [S/N]: ').upper().strip()[0]
print(f'Você digitou {c} números e a média foi de {soma/c:.2f}\n'
      f'O maior valor foi {maior} e o menor foi {menor}')