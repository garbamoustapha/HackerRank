n = int(input())
a = list(map(int, input().split()))

haseven = False
for i in range(n):
    if a[i] % 2 == 0:
        haseven = True
        break
      
hasodd = False
for i in range(n):
    if a[i] % 2 == 1:
        hasodd = True
        break

if haseven and hasodd:
    a.sort()

print(*a)