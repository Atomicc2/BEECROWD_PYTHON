n = int(input())
operacao = input()
linhas = []
colunas = []
for i in range(12):
    for i in range(12):
        x = float(input())
        colunas.append(x)
    linhas.append(colunas.copy())
    colunas.clear()

soma = 0
for i in range(len(linhas)):
    if linhas[i][n]:
        soma += linhas[i][n]

if operacao == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma / 12:.1f}')