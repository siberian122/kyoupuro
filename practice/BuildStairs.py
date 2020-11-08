n=int(input())
h=list(map(int,input().split()))
for i in range(n-1):
    if h[i]==h[i+1]+1:
        h[i]-=1
ans='Yes'
for i in range(n-1):
    if h[i]>h[i+1]:
        ans='No'
        break
#print(h)
print(ans)