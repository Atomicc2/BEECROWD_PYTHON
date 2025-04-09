
lista = []
for i in range(10):
    x = int(input())
    if x > 0:
        lista.append(x)
    else:
        lista.append(1)

for i in range(10):
    print(f'X[{i}] = {lista[i]}')