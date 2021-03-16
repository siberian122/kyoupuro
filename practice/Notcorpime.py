n = int(input())
x = list(map(int, input().split()))
sosu = []


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append(i)

    if temp != 1:
        arr.append(temp)

    if arr == []:
        arr.append(n)

    return arr


for i in x:
    for j in factorization(i):
        if j not in sosu:
            sosu.append(j)
ans = 1
for i in sosu:
    ans *= i


print(sosu)
print(ans)
