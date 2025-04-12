while True:
    entry = int(input())
    if entry == 0:
        break
    for i in range(entry):
        cont = 1
        for j in range(entry):
            print(cont, end=' ')
            cont *= 2
        
        print()
    print()