"""
Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se
elas podem formar um triângulo.
"""
print('=-' * 15)
print('Analizador de Triângulos'.center(30))
print('=-' * 15)
l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos acima PODEM FORMAR um triângulo.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')
