a, b, c = sorted(map(int, input().split()))
if a == b and b != c:
    print("Yes")
elif a != b and b == c:
    print("Yes")
else:
    print("No")
