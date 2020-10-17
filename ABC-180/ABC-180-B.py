n=int(input())
x=list(map(int,input().split()))
man=0
yu=0
ty=0

for i in x:
    num=abs(i)
    man+=num
    yu+=num**2
    ty=max(ty,num)
yu=yu**0.5
print(man)
print(yu)
print(ty)