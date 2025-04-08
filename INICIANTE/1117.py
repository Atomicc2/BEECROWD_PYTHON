cont = 0
soma = 0
while True:
    nota  = float(input())
    if nota >= 0 and nota <= 10:
        cont += 1
        soma += nota
    else:
        print('nota invalida')

    if cont == 2:
        break

print(f'media = {soma / cont:.2f}')