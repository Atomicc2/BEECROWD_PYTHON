'''
0 - 400.00                  15
400.01 - 800.00             12
800.01 - 1200.00            10
1200.01 - 2000.00           7
Acima de 2000.00            4

Novo salario: 460.00
Reajuste ganho: 60.00
Em percentual: 15 %
'''

value = float(input())

if 0 <= value <= 400:
    percentage = 15
if 400 < value <= 800:
    percentage = 12
if 800 < value <= 1200:
    percentage = 10
if 1200 < value <= 2000:
    percentage = 7
if value > 2000:
    percentage = 4

newSalary = value * (percentage / 100 + 1)
adjustment = value * (percentage / 100)


print(f"Novo salario: {newSalary:.2f}")
print(f"Reajuste ganho: {adjustment:.2f}")
print(f"Em percentual: {percentage} %")
