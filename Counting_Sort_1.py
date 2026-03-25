n = int(input())
arr = list(map(int, input().split()))

ind = [0] *  n

for i in range(n):
    ind[arr[i]] += 1

print(*ind)