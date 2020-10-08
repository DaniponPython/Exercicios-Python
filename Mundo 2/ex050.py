"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, descondidere-o
"""
soma = 0
cont = 0
for n in range(1, 7):
    num = int(input(f'Digite o {n}º número inteiro: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} números PARES e a soma destes é igual a {soma}.')
