try:

    while True:
        n = int(input())
        entry = list(map(int, input().split()))
        bigFast = entry[0]
        for i in entry:
            if i > bigFast:
                bigFast = i
        if bigFast < 10:
            print('1')
        elif bigFast >= 10 and bigFast < 20:
            print('2')
        else:
            print('3')

except EOFError:
    pass