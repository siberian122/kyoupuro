x, y = map(int, input().split())
x, y = min(x, y), max(x, y)
if x + 3 > y:
    print("Yes")
else:
    print("No")
