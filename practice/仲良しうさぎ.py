n=int(input())
a=list(map(int,input().split()))
num=0
for i in range(n):
    if a[a[i]-1]==i+1:
        num+=1
    #print(a[a[i]-1],i+1)
print(num//2)
