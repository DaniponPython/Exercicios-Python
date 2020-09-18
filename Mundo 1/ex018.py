"""
18 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do
seno, cosseno e tangente desse ângulo.
"""
from math import sin, cos, tan, radians

ang = int(input('Digite o ângulo que você deseja: '))

print(f"O ângulo de \033[4;36m{ang}\033[m tem o \033[31mSENO de "
      f"{sin(radians(ang)):.1f}.\033[m")
print(f'O ângulo de \033[4;36m{ang}\033[m tem o \033[31mCOSSENO de '
      f'{cos(radians(ang)):.1f}\033[m')
if ang == 90 or ang == 270:
    print(f'Não existe tangente do ângulo de \033[4;36m{ang}\033[m')
else:
    print(f'O ângulo de \033[4;36m{ang}\033[m tem a \033[31mTANGENTE de '
          f'{tan(radians(ang)):.1f}\033[m')
