a, b ,c = map(float, input().split())

if (a + b) <= c or (a + c) <= b or (c + b) <= a:
    area = ((a + b) / 2) * c
    print(f"Area = {area:.1f}")
else:
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")