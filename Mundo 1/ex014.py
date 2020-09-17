"""
Escreva um programa que converta uma temperatura digitando em graus Celsius e
converta em para graus Fahrenheit
"""
temp = int(input('Informe a temperatura em C: '))
fahr = (temp * 9/5) + 32
print(f'A temperatura de \033[2;34m{temp}C\033[m corresponde a '
      f'\033[2;31m{fahr:.0f}F\033[m.')
