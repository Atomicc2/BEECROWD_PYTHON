try: 
    while True:
        n = input()
        if n.isnumeric():
            n = int(n)
            if n > 0:
                print('vai ter duas!')
            else:
                print('vai ter copa!')
except EOFError:
    pass