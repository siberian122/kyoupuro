n, s, d = map(int, input().split())
ans = "No"
for i in range(n):
    x, y = map(int, input().split())
    if x < s and y > d:
        ans = "Yes"
        break
print(ans)
