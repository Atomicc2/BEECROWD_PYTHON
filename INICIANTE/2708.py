total = {
    'output': 0,
    'back': 0,
    'totalOutput': 0,
    'totalBack': 0,
}

while True:
    
    entry = list(input().split())
    if entry[0] == 'ABEND':
        break

    numPeaple = int(entry[1])

    if entry[0] == 'SALIDA':
        total['output'] += 1
        total['totalOutput'] += numPeaple
    else:
        total['back'] += 1
        total['totalBack'] += numPeaple
    entry.clear()

print(total['totalOutput'] - total['totalBack']) 
print(total['output'] - total['back'])