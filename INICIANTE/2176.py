entry = input()
total = []
for i in entry:
    if i == '1':
        total.append(i)

if len(total) % 2 == 0:
    print(entry + '0')
else:
    print(entry + '1')
