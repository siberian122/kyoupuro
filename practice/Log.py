n = int(input())
low = 1
high = n+1
while low < high:
    mid = (low+high)//2
    if (mid+1)*mid//2 > n+1:
        high = mid
    else:
        low = mid+1
ans = n+1-(high-1)
print(ans)
4
