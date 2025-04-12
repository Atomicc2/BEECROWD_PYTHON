operacao = input()
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
        if j < i:
            soma += matriz[i][j]

if operacao == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma / 66:.1f}')
