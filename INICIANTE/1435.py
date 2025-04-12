while True:
    n = int(input())
    if n == 0:
        break

    tam = n

    for i in range(tam):
        for j in range(tam):
            # Calcula a "camada" com base na menor distância da borda
            valor = 1 + min(i, j, tam - 1 - i, tam - 1 - j)

            # Imprime o valor com largura fixa
            print(valor, end=' ' if j < tam - 1 else '')
        print()
    print()

### OBS(CODE VIA CHAT GPT, NÂO CONSEGUI FAZER NEM ENTENDER)