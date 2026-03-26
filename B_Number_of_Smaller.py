m, n = map(int, input().split())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

p = 0
res = []

for v in b:
    while p < m and a[p] < v:
        p += 1
    res.append(str(p))

print(*res)