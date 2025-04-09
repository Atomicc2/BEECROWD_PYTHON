s = 0
cont = 0
for i in range(1, 40, 2):
    s += (i / (2 ** cont))
    cont += 1
print(f'{s:.2f}')