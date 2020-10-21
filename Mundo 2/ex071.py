"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No início,
pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o
programa vai informar quantas cédulas de cada serão entregues.
OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1
"""
print('=' * 20)
print('     BANCO CEV')
print('=' * 20)
valor = int(input('Qual valor você quer sacar? R$ '))
cedula_atual = 50  # maior cedula disponível
total_cedula = 0
while True:
    if valor >= cedula_atual:
        total_cedula += 1
        valor -= cedula_atual
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R${cedula_atual:.2f}')
        if cedula_atual == 50:  # se o valor não é mais igual ou maior que 50,
            # o valor da cédula atual passará a ser 20
            cedula_atual = 20
        elif cedula_atual == 20:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 1
        total_cedula = 0
        if valor == 0:
            break

print('=' * 20)
print('Volte sempre ao Banco CEV')
