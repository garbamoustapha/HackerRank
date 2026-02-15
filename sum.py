import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    pointer = 1
    
    for _ in range(t):
        a = int(input_data[pointer])
        b = int(input_data[pointer + 1])
        c = int(input_data[pointer + 2])
        pointer += 3
        
        if a + b == c or a + c == b or b + c == a:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()