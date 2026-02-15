import sys

def solve():
    line = sys.stdin.readline()
    if not line:
        return
    
    w = int(line.strip())
    
    if w > 2 and w % 2 == 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()