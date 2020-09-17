"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
salário com 15% de aumento
"""
salario = float(input('Qual é o salário do funcionário? R$ '))
print(f'Um funcionário que ganhava \033[31mR$ {salario:.2f}\033[m, com aumento'
      f' de \033[33m15%\033[m, passa a receber \033[34mR$ '
      f'{salario * 1.15:.2f}\033[m.')
