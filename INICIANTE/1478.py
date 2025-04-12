while True:
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        for j in range(n):
            valor = 1 + abs(i - j)
            print(valor, end=' ' if j < i - 1 else '')
        print()
    print()

## OBS(CÓDIGO DO CHATGPT, NÃO FIZ E NEM ENTENDI ESSE)