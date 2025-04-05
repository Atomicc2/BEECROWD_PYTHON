NC = int(input())

lista = {}
total = 0
for i in range(NC):
    quant, tipo = input().split()
    quant = int(quant)
    total += quant
    if tipo in lista:
        lista[tipo] += quant
    else:
        lista[tipo] = quant

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {lista['C']}')
print(f'Total de ratos: {lista['R']}')
print(f'Total de sapos {lista['S']}')
print(f'Percentual de coelhos: {100 * lista['C'] / total:.2f} %')
print(f'Percentual de ratos: {100 * lista['R'] /total:.2f} %')
print(f'Percentual de sapos: {100 * lista['S'] /total:.2f} %')
