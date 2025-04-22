num_total = int(input())

num_possuidas = int(input())

album = []

for i in range(num_possuidas):
    n = int(input())
    if n not in album:
        album.append(n)

print(num_total - len(album))