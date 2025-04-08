def tryAgain():
    print('Novo grenal (1-sim 2-nao)')
    resp = int(input())
    if resp == 1:
        return True
    if resp == 2:
        return False
    
grenaisInter = grenaisGremio = empates = cont = 0
new = True
while new:
    inter, gremio = map(int, input().split())
    cont += 1
    if inter > gremio:
        grenaisInter += 1
    elif gremio > inter:
        grenaisGremio += 1
    else:
        empates += 1
    new = tryAgain()

print(f'{cont} grenais')
print(f'Inter:{grenaisInter}')
print(f'Gremio:{grenaisGremio}')
print(f'Empates:{empates}')
if grenaisInter > grenaisGremio:
    print('Inter venceu mais')
elif grenaisGremio > grenaisInter:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')