def josephus(n, k):
    res = 0
    for i in range(2, n + 1):
        res = (res + k) % i
    return res + 1

nc = int(input())

for case in range(1, nc + 1):
    n, k = map(int, input().split())
    result = josephus(n, k)
    print(f"Case {case}: {result}")