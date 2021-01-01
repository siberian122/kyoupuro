a = list(map(int, input().split()))
a.sort()
ans = 0
ans += abs(a[1]-a[0])
ans += abs(a[2]-a[1])
print(ans)
