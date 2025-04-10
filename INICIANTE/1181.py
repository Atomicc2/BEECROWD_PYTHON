n = int(input())
operacao = input()
linhas = []
colunas = []
for i in range(12):
    for j in range(12):
        num = float(input())
        colunas.append(num)
    linhas.append(colunas.copy())
    colunas.clear()

soma = 0
for i in range(len(linhas[n])):
    soma += linhas[n][i]

if operacao == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma / 12:.1f}')