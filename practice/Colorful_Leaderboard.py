n=int(input())
rate=list(map(int,input().split()))
color=[0 for i in range(9)]
for i in rate:
    if i>=3200:
        color[-1]+=1
    else:
        color[i//400]+=1
ans=0
for i in range(8):
    if color[i]>0:
        ans+=1
print(1,color[-1]) if ans==0 else print(ans,ans+color[-1])

