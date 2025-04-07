N = int(input())
temp = 0
for i in range(N):
    soma = 0
    x, y = map(int, input().split())
    if y > x:
        temp = x
        x = y
        y = temp
    for i in range(x + 1, y ):
        if i % 2 == 1:
            soma += i
    print(soma)
