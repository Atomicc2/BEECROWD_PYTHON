n1 = 0
n2 = 1
lista = [n1, n2]

for i in range(59):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    lista.append(n3)

n = int(input())
for i in range(n):
    value = int(input())
    print(f'Fib({value}) = {lista[value]}')