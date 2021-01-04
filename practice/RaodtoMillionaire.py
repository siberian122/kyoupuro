n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n-1):
    num = a[i]-a[i+1]
    b.append(num)
now = 1000
stock = 0
for i in range(n-1):
    if b[i] > 0:  # 売る
        now += stock*a[i]
        stock = 0
    elif now > 0 and b[i] < 0:  # 買う
        stock += now//a[i]
        now = now % a[i]
    #print(now, stock)
now += a[-1]*stock
print(now)
