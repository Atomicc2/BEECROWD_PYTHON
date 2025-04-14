#Jeito fácil usando funções especificas do python
'''n = int(input())
hexa = hex(n).replace('0x', '').upper()
print(hexa)'''

#Jeiro dificil manipulando listas em python
n = int(input())

baseHex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
result = []

while n > 0:
    result.append(baseHex[(n % 16)])
    n //= 16

for i in range(len(result) - 1, -1, -1):
    print(result[i], end='')