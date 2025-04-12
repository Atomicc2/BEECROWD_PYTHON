n = input()

matriz = []
coluna = []

for i in range(12):
    for j in range(12):
        x = float(input())
        coluna.append(x)

    matriz.append(coluna.copy())
    coluna.clear()

soma = 0
for i in range(12):
    for j in range(12):
        if i > j and i + j > 11:
            soma += matriz[i][j]

if n == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma / 30:.1f}')