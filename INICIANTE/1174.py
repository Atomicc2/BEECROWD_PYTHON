
lista = []
for i in range(100):
    value = float(input())
    lista.append(value)

for i in range(100):
    if lista[i] <= 10:
        print(f'A[{i}] = {lista[i]}')