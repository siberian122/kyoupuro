n,W=map(int,input().split())
wv=[]
for i in range(n):
    wv.append(list(map(int,input().split())))
inf=float('inf')
dp=[[-inf for i in range(W+1)] for j in range(n+1)]
for i in range(W+1):
    dp[0][i]=0
for i in range(n):
    for w in range(W+1):
        if wv[i][0]<=w:
            dp[i+1][w]=max(dp[i][w-wv[i][0]]+wv[i][1], dp[i][w])
            '''
            weightがw未満の時に追加←選ばないほうが良い時もあるからmax()で選ばない時と比較
            [w-wv[i][0]]はそのweightの時の最大のwまでをvalueで埋めるため
            最大wまで埋めてほかのものをとって更新できるかをみる
            '''
        else:
            dp[i+1][w]=dp[i][w]
print(dp[n][W])