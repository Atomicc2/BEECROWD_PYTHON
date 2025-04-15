try:
    while True:
        cont = 0
        NC, ID = map(int, input().split())
        for i in range(NC):
            pubId, game = map(int, input().split())
            if pubId == ID:
                if game == 1:
                    cont += 1
        print(cont)
except EOFError:
    pass