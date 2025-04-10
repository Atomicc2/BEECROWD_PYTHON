n = int(input())
lista = [n]
for i in range(9):
    n *= 2
    lista.append(n)

for i in range(10):
    print(f'N[{i}] = {lista[i]}')