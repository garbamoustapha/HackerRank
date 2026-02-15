n = int(input())

phone_book = {}
for _ in range(n):
    entry = input().split()
    phone_book[entry[0]] = entry[1]

while True:
    try:
        query = input().strip()
        
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
            
    except EOFError:
        break