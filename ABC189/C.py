n = int(input())
a = list(map(int, input().split()))
ans = []
for i, j in enumerate(a):
    num = i
    for l in range(i+1, n):
        if j > a[l]:
            num = l
            break
    if num == i:
        num = n
    ans.append(j*(num-i))
print(max(ans))
