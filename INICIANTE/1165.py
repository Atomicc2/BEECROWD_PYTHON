n = int(input())

for case in range(n):
    value = int(input())
    cont = 0
    for i in range(1, value + 1):
        if value % i == 0:
            cont += 1
    if cont == 2:
        print(f'{value} eh primo')
    else:
        print(f'{value} nao eh primo')