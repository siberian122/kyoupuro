n = int(input())
a = list(map(int, input().split()))
A = [0] * 401
for i in a:
    A[i+200] += 1
ans = 0
for i in range(1, 401):
    for j in range(i):
        ans += A[i]*A[j]*((j-i)**2)
print(ans)
