NC = int(input())

lista = list(map(int, input().split()))

smaller = lista[0]
position = 0

for i in range(0, len(lista)):
    if lista[i] < smaller:
        smaller = lista[i]
        position = i 

print(position + 1)