a, b, c = map(float, input().split())

lista = [a, b, c]
lista.sort(reverse=True)
A = lista[0]
B = lista[1]
C = lista[2]

if A >= (B + C):
    print("NAO FORMA TRIANGULO")
else:
    if (A ** 2) == ((B ** 2) + (C ** 2)):
        print("TRIANGULO RETANGULO")
    if (A ** 2) > ((B ** 2) + (C ** 2)):
        print("TRIANGULO OBTUSANGULO")
    if (A ** 2) < ((B ** 2) + (C ** 2)):
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif (A == B) or (A == C) or (B == C):
        print("TRIANGULO ISOSCELES")