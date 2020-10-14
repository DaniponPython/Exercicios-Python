"""
Melhore o desafio 051, perguntadno para o usuário se ele quer mostrar mais
alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
"""
print('Gerador de PA')
print('-=' * 10)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
total = 0
contador = 0
mais_termos = 10

while mais_termos != 0:

    while contador < mais_termos:
        print(primeiro, end=' -> ')
        contador += 1
        primeiro += razao
        total += 1
    print('PAUSA')
    mais_termos = int(input('Quantos termos você quer mostrar a mais? '))
    contador = 0

print(f'Progressão finalizada com {total} termos mostrados.')
print('FIM')
