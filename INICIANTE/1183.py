opreacao = input()
linha = []
coluna = []
for i in range(12):
    for j in range(12):
        x = float(input())
        coluna.append(x)

    linha.append(coluna.copy())
    coluna.clear()

soma = 0
for i in range(12):
    for j in range(12):
        if j > i:
            soma += linha[i][j]

if opreacao == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma / 66:.1f}')