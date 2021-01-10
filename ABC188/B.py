n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
num = 0
for i in range(n):
    num += a[i]*b[i]
if num:
    print("No")
else:
    print("Yes")
