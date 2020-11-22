n=int(input())
s=list(map(int,input().split()))
a=[0 for _ in range(2*10**5+1)]
for i in s:
    a[i]+=1
all_col=0
for i in range(len(a)):
    all_col+=int(a[i]*(a[i]-1)/2)
for i in range(n):
    print(all_col-(a[s[i]]-1))