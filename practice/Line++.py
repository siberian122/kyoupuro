n,x,y=map(int,input().split())
x-=1
y-=1
L=[0 for _ in range(n)]
for i in range(n-1):
    for j in range(i+1,n):
        dis=min(j-i,abs(x-i)+1+abs(y-j))
        #最小値(橋を使わない,橋を使う)
        #橋を使う➞橋(左)までの距離+1(橋を渡る)+橋(右)からの距離
        L[dis]+=1

for k in range(1,n):
    print(L[k])