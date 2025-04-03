n1, n2, n3 = map(int, input().split())

lista = [n1, n2, n3]
for i in range(3):
    listaTemp = sorted(lista)
    print(listaTemp[i])
print()
for i in range(3):
    print(lista[i])