"""
Faça um programa que leia um número inteiro e mostre na tela o seu antecessor e
o seu sucessor
"""
num = int(input('Digite um número: '))
print(f'Analisando o número \033[34m{num}\033[m, o seu antecessor é'
      f' \033[32m{num - 1}\033[m e seu sucessor é \033[31m{num + 1}\033[m.')
