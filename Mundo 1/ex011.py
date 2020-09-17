"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule
a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada
litro de tinta pinta uma área igual a 2 metros quadrados.
"""
larg = float(input('Largura da parede (m): '))
alt = float(input('Altura da parede (m): '))
area = larg * alt
tinta = area / 2
print(f'Sua parede tem a dimensão de \033[31m{larg:.2f}\033[m X '
      f'\033[31m{alt:.2f}\033[m e sua área é de \033[34m{area:.2f}\033[m m2.')
print(f'Para pintar essa parede, vocÊ precisará de \033[34m{tinta:.2f}\033[m '
      'litros de tinta.')
