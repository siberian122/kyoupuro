n=int(input())
a=list(map(int,input().split()))
cnt=0
X=max(a)
x=min(a)
cnt=0
while a:
    x=min(a)
    a=[a[i]%x for i in range(len(a)) if a[i]%x !=0]
print(x)
'''
#print(*aa)
x=min(aa)
X=max(aa)
aaa=[aa[i]%x for i in range(len(aa)) if aa[i]%x != 0]
print(aaa)

print(x)
'''