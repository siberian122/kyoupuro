n = int(input())
s = input()
cnt = ""
ans = 0
for i in s:
    if cnt == i:
        ans += 1
    else:
        cnt = i
print(n-ans)
