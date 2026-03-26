s, l = map(int, input().split())
n = list(map(int, input().split()))

left = 0
right = 0
cs = 0
answer = 0

while right < len(n):
    cs += n[right]

    while cs > l and left <= right:
        cs -= n[left]
        left += 1

    cl = right - left + 1
    if cl > answer:
        answer = cl

    right += 1

print(answer)
