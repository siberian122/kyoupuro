k=int(input())
x=0
ans=0
for i in range(1,k+1):
    x=(10*x+7)%k
    if x==0:
        ans=i
        break
if ans:
    print(ans)
else:
    print(-1)