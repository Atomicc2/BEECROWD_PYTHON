while True:
    NC = int(input())
    if NC == 0:
        break
    for i in range(NC):
        notes = list(map(int, input().split()))
        letters = {
            'A': notes[0],
            'B': notes[1],
            'C': notes[2],
            'D': notes[3],
            'E': notes[4],
        }
        confirm = []
        for k, v in letters.items():
            if v <= 127:
                confirm.append(k)
        if len(confirm) == 1:
            print(confirm[0])
        else:
            print('*')