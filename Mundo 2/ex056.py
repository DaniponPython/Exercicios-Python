"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do
programa mostre:
-> A média de idade do grupo.
-> Qual é o nome do homem mais velho.
-> Quantas mulheres tem menos de 20 anos.
"""

media = mulher_nova = idade_velho = conta_homem = 0
nome_velho = ''

for p in range(1, 5):
    print(f'---- {p}ª pessoa ----')
    nome = input('Nome: ').title()
    idade = int(input('Idade: '))
    sexo = input('Sexo [F/M]: ').upper()
    media += idade

    if sexo == 'F':
        if idade < 20:
            mulher_nova += 1

    if sexo == 'M':
        conta_homem += 1
        if idade > idade_velho:
            idade_velho = idade
            nome_velho = nome

print(f'A média de idade do grupo é de {media/4:.2f} anos')
if mulher_nova == 0:
    pass
else:
    print(f'Ao todo são {mulher_nova} mulher(es) com menos de 20 anos.')
if conta_homem == 0:
    pass
else:
     print(f'O homem mais velho se chama {nome_velho} e tem {idade_velho} anos.')

