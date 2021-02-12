n = int(input())
ans = 2
for _ in range(n):
    s = input()
    if s == "AND":
        ans += 2
    else:
        ans *= 2
print(ans-1)
