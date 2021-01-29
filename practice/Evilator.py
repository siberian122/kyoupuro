s = input()
n = len(s)
ans = 0
for i in range(n):
    if s[i] == "U":
        ans += n-i-1
        ans += i*2
    else:
        ans += i
        ans += (n-i-1)*2
print(ans)
