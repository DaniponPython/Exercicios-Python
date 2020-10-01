"""
A Confederação Nacional de Natação precisa de um programa wue leia o ano de
nascimento de um atleta e mostre sua categoria, de acordo com a idade:
Até 09 anos - Mirim
Até 14 anos - Infantil
Até 19 anos - Junior
Até 25 anos - Sênior
Acima - Master
"""
from datetime import date

nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÙNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
