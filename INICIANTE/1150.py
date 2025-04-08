x = int(input())
y = x
cont = 1
while True:
    z = int(input())
    if z > x:
        while x <= z:
            x += y + cont
            cont += 1
        break

print(cont)