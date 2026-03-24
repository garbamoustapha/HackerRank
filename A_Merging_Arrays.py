a, b = map(int, input().split())

a1 = list(map(int, input().split()))
b1 = list(map(int, input().split()))

tab = []
j = 0
k = 0

for i in range(a+b):
    if j < a and k <b :
        if j < a and k <b and a1[j] < b1[k]:
            tab.append(a1[j])
            j += 1
        elif a1[j] >= b1[k]:
            tab.append(b1[k])
            k += 1
    else:
        if j < a:
            tab.append(a1[j])
            j += 1
        elif k < b:
            tab.append(b1[k])
            k += 1
        
print(*tab)
