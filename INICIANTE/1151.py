n = int(input())
n -= 2
n1 = 0
n2 = 1
lista = [str(n1), str(n2)]
for i in range(n):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    lista.append(str(n3))

print(' '.join(lista))  
    
