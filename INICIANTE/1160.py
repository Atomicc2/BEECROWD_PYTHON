'''
- objetivo: Saber a quantidade de anos que a cidade A leva para ultrapassar a cidade B
- Só se a taxa de crecimento de A for maior que a de B
- Tempo em anos 
- Para maiores de 100 anos exibir Mais de 1 seculo
### 1 linha de entrada - casos de teste
### Cada caso tem 4 entradas:
# PA - inteiro - população de A
# PB - inteiro - popilação de B
# G1 - float - Percentual de crescimento
# G2 - float - Percentual de crescimento
'''

NC = int(input())

for i in range(NC):
    PA, PB, G1, G2 = map(float, input().split())
    PA = int(PA)
    PB = int(PB)
    cont = 0
    while PA <= PB:
        PA = int(PA * (1 + G1 / 100))
        PB = int(PB * (1 + G2 / 100))
        cont += 1
        if cont > 100:
            break
    if cont > 100:
        print(f'Mais de 1 seculo.')
    else:
        print(f'{cont} anos.')
