yearMother = int(input())
yearSon1 = int(input())
yearSon2 = int(input())

yearSon3 = yearMother - (yearSon1 + yearSon2)

old = yearSon1
if yearSon2 > old:
    old = yearSon2
if yearSon3 > old:
    old = yearSon3
print(old)