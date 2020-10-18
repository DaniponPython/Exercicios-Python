"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só
vai parar quando o usuário digitar o valor 999, que é a condição e parada. No
final mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag.)
"""
s = tot = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    s += num
    tot += 1
print(f'A soma dos {tot} valores foi {s}')
