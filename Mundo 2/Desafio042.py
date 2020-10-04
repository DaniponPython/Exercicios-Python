"""
Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo
de triângulo será formado:
Equilátero: todos os lados iguais
Isósceles: 2 lados iguais
Escaleno: todos os lados diferentes
"""
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    if s1 == s2 == s3:
        print('Os segmentos acima podem formar um triângulo EQUILÁTERO')
    elif s1 != s2 != s3 != s1:
        print('Os segmentos acima podem formar um triângulo ESCALENO')
    else:
        print('Os segmentos acima podem formar um triângulo ISOSCELES')
else:
    print('Os segmentos acima não podem formar um triângulo')
