"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de
fogos de artificios, indo de 10 a zero, com uma pausa de um segundo entre eles.
"""
from time import sleep

for n in range(10, -1, -1):
    print(n)
    sleep(1)
print('BUM! BUM! POOW!')
