s, p = map(int, input().split())
ans = 'No'
for i in range(10**6+100):
    if i*(s-i) == p:
        ans = 'Yes'
        break
print(ans)
