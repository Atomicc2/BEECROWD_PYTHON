# Vão entrar os raios e as posições no plano cartesiano e tenho que ver se o R1 engloba o R2

from math import hypot


try:
    while True:
        r1, x1, y1, r2, x2, y2 = map(int, input().split())

        dis = hypot(x1 - x2, y1 - y2)
        if dis + r2 <= r1:
            print('RICO')
        else:
            print('MORTO')
except EOFError:
    pass