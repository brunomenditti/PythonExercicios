from datetime import date

total_maior = 0
total_menor = 0
for pessoa in range(1, 8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoa)))
    idade = date.today().year - nascimento
    if idade < 21:
        total_menor += 1
    elif idade >= 21:
        total_maior +=1
print('Ao todo tivemos {} pessoas maiores de idade\nE também tivemos {} pessoas menores de idade'.format(total_menor, total_maior))
