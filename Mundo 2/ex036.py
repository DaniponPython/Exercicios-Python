"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma
casa. O programa vai perguntar o valor da casa, o salário do comprador e em
quantos anos ele vai pagar:
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do
salário ou então o empréstimo será negado.
"""
casa = float(input('Valor da casa: R$ '))
sal = float(input('Salário do comprador: R$ '))
fin = int(input('Quantos anos de financiamento? '))
parcela = casa / (fin * 12)
print(f'Para pagar uma casa de R${casa:.2f} em {fin} anos, a prestação será de'
      f'R$ {parcela:.2f}')
if parcela > (sal * 0.3):
    print('Empréstimo NEGADO')
else:
    print('Empréstimo pode ser CONCEDIDO!')
