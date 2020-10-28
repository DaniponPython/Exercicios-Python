"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo
com sua idade:
- Se ele ainda vai se alistar no serviço militar
- Se é a hora de se alistar
- Se já passou do tempo de alistamento
- Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
"""
from datetime import date

ano_nasc = int(input('Ano do seu nascimento: '))
print('Informe o Sexo:\n'
      '[1] Feminino\n'
      '[2] Masculino')
sexo = int(input('Sua opção: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print(f'Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}.')
if sexo == 1:
    print('Você não precisa fazer alistamento militar obrigatório.')
elif sexo == 2:
    if idade < 18:
        print(f'Ainda faltam {18 - idade} anos para seu alistamento.\n'
              f'Seu alistamento será em {(18 - idade) + ano_atual}')
    elif idade > 18:
        print(f'Você já deveria ter se alistado há {idade - 18} anos.\n'
              f'Seu alistamento foi em {ano_atual -(idade - 18)}')
    else:
        print('VocÊ tem que se alistar IMEDIATAMENTE!')
else:
    print('Opção inválida. Tente novamente!')
