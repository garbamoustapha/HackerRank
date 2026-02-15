import sys

def solve():
    data = sys.stdin.read().split()
    
    index_un = data.index('1')
    
    r = index_un // 5
    c = index_un % 5
    
    resultat = abs(r - 2) + abs(c - 2)
    
    print(resultat)

if __name__ == "__main__":
    solve()