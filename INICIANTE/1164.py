N = int(input())
for i in range(N):
    value = int(input())
    soma = 0
    for number in range(1, value):
        if value % number == 0:
            soma += number
    if value == soma:
        print(f'{value} eh perfeito')
    else:
        print(f'{value} nao eh perfeito')