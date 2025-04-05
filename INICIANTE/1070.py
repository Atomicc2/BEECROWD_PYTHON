n = int(input())

for i in range(6):
    if n % 2 == 1:
        print(i)
        n += 2 
    else:
        n += 1
        print(i)
        n += 2
        