"""
Faça um programa que calcule a soma entre todos os números ímpares que são
múltiplos de três e que se encontram um intervalo de 1 até 500.
"""
soma = 0
contador = 0

for n in range(3, 500, 3):
    if n % 2 == 1:
        soma += n
        contador += 1
print(f'A soma de todos os {contador} valores solicitados é igual a {soma}. ')
