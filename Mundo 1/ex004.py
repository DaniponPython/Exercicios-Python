"""
Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo
e todas as informações possíveis sobre ele
"""
algo = input('Digite algo: ')
cor = {
    'clear': '\033[m',
    'red': '\033[31m',
    'green': '\033[32m',
}
print(f'O tipo primitivo é: {cor["green"]}{type(algo)}{cor["clear"]}\n'
      f'Só tem espaço? {cor["red"]}{algo.isspace()}{cor["clear"]}\n'
      f'É um número? {cor["red"]}{algo.isnumeric()}{cor["clear"]}\n'
      f'É alfabeto? {cor["red"]}{algo.isalpha()}{cor["clear"]}\n'
      f'É alfanumérico? {cor["red"]}{algo.isalnum()}{cor["clear"]}\n'
      f'Está em minúscula? {cor["red"]}{algo.islower()}{cor["clear"]}\n'
      f'Está capitalizada? {cor["red"]}{algo.istitle()}{cor["clear"]}\n')
