x, y = map(int, input().split())
cont = 1
while cont <= y:
    linha = []
    for j in range(x):
        linha.append(str(cont))
        cont += 1
    print(' '.join(linha))