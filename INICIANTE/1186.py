'''n = input()
matriz = []
coluna = []
soma = 0
for i in range(12):
    for j in range(12):
        x = float(input())
        coluna.append(x)

    matriz.append(coluna.copy())
    coluna.clear()

    for k in range(12):
        if (i + k) > 11:
            soma += matriz[i][k]

if n == 'S':
    print(f'{soma}')
else:
    print(f'{soma / 66:.1f}')'''

n = input()
soma = 0
for i in range(12):
    for j in range(12):
        x = float(input())
        if (i + j) > 11:
            soma += x
if n == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma /66:.1f}')