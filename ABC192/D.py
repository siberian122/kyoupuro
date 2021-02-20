x = int(input())
m = int(input())

N = int(max(str(x))) + 1
ans = []
while int(str(x), N) <= m:
    ans .append(int(str(x), N))
    N += 1
ans = set(ans)

print(len(ans))
