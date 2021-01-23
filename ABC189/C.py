n = int(input())
a = list(map(int, input().split()))
ans = []
for i, j in enumerate(a):
    num = i
    num = a.index()
    if num == i:
        num = n
    ans.append(j*(num-i))
print(max(ans))
