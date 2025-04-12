import math

while True:
    entrada = input()
    if entrada == '0':
        break

    a, b, c = map(int, entrada.split())
    area_casa = a * b
    terreno_total = area_casa * 100 / c
    lado_terreno = math.ceil(math.sqrt(terreno_total))
    print(lado_terreno)
