###  Divisão da Nlogônia ###

# Vou receber varios dados:
# Primeiro o NC (Número de Casos)
# Depois as coodenadas centrais
# Depois as coordenadas das residências
# Retorno a posição da casa

while True:
    NC = int(input())
    if NC == 0:
        break
    x, y = map(int, input().split())
    for i in range(NC):
        xr, yr = map(int, input().split())
        if xr == x or yr == y:
            print('divisa')
        elif xr < x and yr > y:
            print('NO')
        elif xr > x and yr > y:
            print('NE')
        elif xr > x and yr < y:
            print('SE')
        elif xr < x and yr < y:
            print('SO')