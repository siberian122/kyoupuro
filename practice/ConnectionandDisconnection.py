s = input()
k = int(input())
ans = 0

if len(set(s)) == 1:
    exit(print(len(s)*k//2))
a = [1]
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        a[-1] += 1
    else:
        a.append(1)
for i in a:
    ans += i//2
ans *= k
if s[0] == s[-1] and a[0] % 2 == a[-1] % 2 == 1:
    ans += k-1
print(ans)
