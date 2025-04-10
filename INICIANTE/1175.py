lista = []
for i in range(20):
    value = int(input())
    lista.append(value)

for i in range(10):
    temp = lista[i]
    lista[i] = lista[-i - 1]
    lista[-i - 1] = temp

for i in range(20):
    print(f'N[{i}] = {lista[i]}')