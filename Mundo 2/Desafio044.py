"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando
o seu preço normal e condição de pagamento:
a vista dinheiro/cheque: 10% de desconto
a vista no cartão: 5% de desconto
em até 2 vezes no cartão: preço normal
3 x ou mais no cartão: 20% de juros
"""
print('============ LOJAS JUDITE ============')
valor = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO\n'
      '\t[ 1 ] à vista dinheiro/cheque\n'
      '\t[ 2 ] à vista cartão\n'
      '\t[ 3 ] 2x no cartão\n'
      '\t[ 4 ] 3x ou mais no cartão')
pgto = int(input('Sua opção: '))
if pgto == 1:
    print(f'Sua compra de R${valor:.2f} vai custar R${valor*.9:.2f} no final.')
elif pgto == 2:
    print(f'Sua compra de R${valor:.2f} vai custar R${valor*0.95:.2f} no final.')
elif pgto == 3:
    print(f'Sua compra será parcelada em 2x de R${valor/2:.2f} SEM JUROS.')
elif pgto == 4:
    parcela = int(input('Quantas parcelas: '))
    print(f'Sua compra será parcelada em {parcela}x de R${(valor/parcela)*1.2:.2f} COM JUROS\n'
          f'Sua compra de R$ {valor:.2f} vai custar R$ {valor * 1.2:.2f} no final.')
else:
    print('Opção inválida. Tente novamente!')