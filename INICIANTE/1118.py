
cont = soma = 0
again = True
while again:
    nota = float(input())
    if 0 <= nota <= 10:
        cont += 1
        soma += nota
    else:
        print('nota invalida')
    
    if cont == 2:
        print(f'media = {soma / cont:.2f}')
        cont = soma = 0
        while True:
            resp = int(input('novo calculo (1-sim 2-nao)'))
            if resp == 1:
                again = True
                break
            elif resp == 2:
                again =  False  
                break