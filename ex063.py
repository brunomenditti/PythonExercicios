'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma SEQUÊNCIA DE FIBONACCI.
Ex 0 → 1 → 1 → 2 → 3 → 5 → 8'''

termo = int(input('Quantos termos você quer mostrar? '))
termo1 = 0
termo2 = 1
cont = 3
while cont <= termo:
    termo3 = termo1 + termo2
    print('{} → '.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    cont += 1
print('Fim')
