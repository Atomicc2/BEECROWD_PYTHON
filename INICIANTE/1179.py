par = []
impar = []
for i in range(15):

    x = int(input())

    if x % 2 == 0:
        par.append(x)
        if len(par) == 5:
            for i in range(5):
                print(f'Par[{i}] = {par[i]}')
            par.clear()

    elif x % 2 == 1:
        impar.append(x)
        if len(impar) == 5:
            for i in range(5):
                print(f'Impar[{i}] = {impar[i]}')
            impar.clear()

for i in range(len(impar)):
    print(f'Impar[{i}] = {impar[i]}')

for i in range(len(par)):
    print(f'Par[{i}] = {par[i]}')


