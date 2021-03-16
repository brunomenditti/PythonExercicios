'''Crie um programa que leia vários números inteiros pelo teclado. No fianl da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores'''
resposta = 'S'
soma = 0
cont = 0
maior = 0
menor = 0
media = 0
while resposta in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resposta = str(input('Quer continusar? [S/N]: ')).upper().strip()[0]
media = soma / cont
print('Você digitou {} numeros e a média foi {:.2f}'.format(cont, media))
print('O maior número é {} e o menor é {}'.format(maior, menor))
