n = int(input())
a = sorted(list(map(int, input().split())))
mod = 998244353
ans = 0
c = 0
for i in a:
    ans = (ans + (c+i)*i) % mod
    c = (c*2+i) % mod
print(ans)
