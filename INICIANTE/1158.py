n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    if x % 2 == 0:
        x += 1
    z = x
    for i in range(y - 1):
        z = z + 2
        x += z
    print(x)
        