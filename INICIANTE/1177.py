n = int(input())
lista = []
x = 0
for i in range(1000):
    if x == n:
        x = 0
    lista.append(x)
    x += 1
    print(f'N[{i}] = {lista[i]}')
