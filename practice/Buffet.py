n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = 0
mae = n
for i in a:
    ans += b[i-1]
    if mae+1 == i:
        ans += c[mae-1]
    mae = i
    # print(ans)
print(ans)
