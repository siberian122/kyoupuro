n=list(input())
n=[int(x) for x in n]
num=sum(n)
cnt=0
if num%3==0:
    exit(print(0))
elif num%3==1:
    for i in n:
        if i%3==1 and len(n)>1:
            exit(print(1))
        elif i%3==2:
            cnt+=1
else:
    for i in n:
        if i%3==2 and len(n)>1:
            exit(print(1))
        elif i%3==1:
            cnt+=1
if cnt>1 and len(n)>2:
    exit(print(2))
print(-1)