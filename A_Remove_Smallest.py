t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr = sorted(arr)
    f = True
    for i in range(n-1):
        if abs(arr[i] - arr[i+1]) > 1:
            print("NO")
            f = False
            break

    if f:
        print("YES")