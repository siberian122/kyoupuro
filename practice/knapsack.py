N,W=map(int,input().split())
item=[]
for _ in range(N):
    item.append(list(map(int,input().split())))

dp=[0 for _ in range(W+1)]
for w,v in item:
    for i in range(w,W+1)[::-1]:
        tmp=dp[i-w]+v
        if tmp>dp[i]:
            dp[i]=tmp
print(dp)
print(max(dp))