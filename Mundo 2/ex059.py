"""
Crie um programa que leia dois valores e mostre um menu na tela
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] encerrar programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

from time import sleep

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opcao = ''

while opcao != '5':
    print('\t[ 1 ] Somar\n'
          '\t[ 2 ] Multiplicar\n'
          '\t[ 3 ] Maior\n'
          '\t[ 4 ] Novos números\n'
          '\t[ 5 ] Sair do programa')
    opcao = input('Qual sua opção? ')

    if opcao == '1':
        print(f'A soma entre {num1} + {num2} é  {num1 + num2}')

    elif opcao == '2':
        print(f'O resultado de {num1} x {num2} é {num1 * num2}')

    elif opcao == '3':
        if num1 > num2:
            print(f'Entre {num1} e {num2} o maior valor é {num1}')
        else:
            print(f'Entre {num1} e {num2} o maior valor é {num2}')

    elif opcao == '4':
        print('Informe os números novamente:')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))

    elif opcao == '5':
        print('Finalizando...')

    else:
        print('Opção inválida. Tente novamente.')

    print('-=' * 20)
    sleep(2)
    
print('Fim do programa! Volte sempre!')
