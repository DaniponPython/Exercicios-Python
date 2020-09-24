"""
26 - Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "A"
Em que posição ela aparece pela primeira vez
Em que posição ela aparece pela última vez
"""
frase = input('Digite uma frase: ').strip().upper()
print(f'A letra A aparece {frase.count("A")} vezes.\n'
      f'A primeira letra A apareceu na posição {frase.find("A") + 1}\n'
      f'A última letra A apareceu na posição {frase.rfind("A") + 1}')
