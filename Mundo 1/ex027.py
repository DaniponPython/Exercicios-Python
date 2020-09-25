"""
27 - Faça um programa que leia o nome completo de uma pessoa, mostrando em
seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
último = Souza
"""
nome = input('Digite seu nome completo: ').strip().title()
separa = nome.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {separa[0]}\n'
      f'Seu último nome é {separa[-1]}')
