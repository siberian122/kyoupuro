n,m,x=map(int,input().split())
book=[]
mon=[]
ans=0
for i in range(n):
      cnt=list(map(int,input().split()))
      mon.append(cnt[0])
      book.append(cnt[1:])
min_total=100000000000000
for i in range(2**n):
        a=[0]*m
        total=0
        for j in range(n):
                if ((i >>j)&1):
                        total+=mon[j]
                        for k in range(m):
                                a[k]+=book[j][k]
                if min(a) >=x and min_total>=total:
                        min_total=total
if min_total!=100000000000000:
        print(min_total)
else:
        print('-1')

'''
n,w=map(int,input().split())
wv=[]
for i in range(n):
    wv.append(list(map(int,input().split())))
min_total=0
for i in range(2**n):
    weight=0
    num=0
    for j in range(n):
        if ((i>>j)&1):
            weight+=wv[j][0]
            num+=wv[j][1]
        if weight<=w and min_total<=num:
            min_total=num

print(min_total)
'''