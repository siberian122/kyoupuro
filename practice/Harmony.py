a, b = sorted(map(int, input().split()))
if a % 2 == b % 2:
    print((b+a)//2)
else:
    print("IMPOSSIBLE")
