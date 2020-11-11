n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=[]
ans.append(min(a[0],b[0]))
for i in range(1,n):
    ans.append(min(a[i+1],b[i]-ans[i-1]))


    