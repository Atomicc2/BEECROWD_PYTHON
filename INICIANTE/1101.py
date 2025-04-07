while True:
    soma = 0
    temp = 0
    x, y = map(int, input().split())
    if x > y:
        temp = x
        x = y
        y = temp
    for i in range(x, y + 1):
        soma += i
        print(f'{i} ', end='')
    print(f'Sum={soma}')
    if x < 0 or y < 0:
        break