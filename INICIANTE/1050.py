from collections import namedtuple

Number = namedtuple('Number', ['ddd', 'destination'])

numbers = {
    Number(61, 'Brasilia'),
    Number(71, 'Salvador'),
    Number(11, 'Sao Paulo'),
    Number(21, 'Rio de Janeiro'),
    Number(32, 'Juiz de Fora'),
    Number(19, 'Campinas'),
    Number(27, 'Vitoria'),
    Number(31, 'Belo Horizonte'),
}

code = int(input())
confirmation = False

for i in numbers:
    if i.ddd == code:
        confirmation = True
        destination = i.destination
if confirmation:
    print(destination)
else:
    print('DDD nao cadastrado')