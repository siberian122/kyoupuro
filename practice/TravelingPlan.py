n = int(input())
a = (list((map(int, input().split()))))
a = [0] + a+[0]
ans = 0
for i in range(n+1):
    ans += abs(a[i]-a[i+1])
for i in range(n):
    print(ans - abs(a[i+1]-a[i]) - abs(a[i+2]-a[i+1])+abs(a[i+2]-a[i]))
