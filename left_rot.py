import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    k = int(input_data[1])
    a = input_data[2:]
    
    k = k % n
    res = a[k:] + a[:k]
    
    print(*(res))

if __name__ == "__main__":
    solve()