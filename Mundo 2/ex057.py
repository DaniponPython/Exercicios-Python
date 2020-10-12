"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'F' e
'M'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
sexo = input('Digite seu sexo: [M/F] ').strip()
while sexo not in 'FfMm':
    sexo = input('Dados inválidos. Por favor, informe seu sexo: ').strip()
print(f'Sexo {sexo.upper()} digitado com sucesso.')
