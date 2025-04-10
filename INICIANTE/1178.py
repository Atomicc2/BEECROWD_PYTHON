x = float(input())
lista = [x]
for i in range(1, 100):
    x /= 2
    lista.append(x)

for i in range(100):
    print(f'N[{i}] = {lista[i]:.4f}')