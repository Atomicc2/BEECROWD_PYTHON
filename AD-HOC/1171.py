NC = int(input())

lista = {}

for i in range(NC):
    n = int(input())
    if n in lista:
        lista[n] += 1
    else:
        lista[n] = 1

for i in sorted(lista.keys()):
    print(f'{i} aparece {lista[i]} vez(es)')