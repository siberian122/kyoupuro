x=int(input())
num=0
ans=[]
for i in range(1,int(x**0.5)+1):
    for j in range(2,int(x**0.5)+2):
        num=i**j
        if num<=x:
            ans.append(num)
        else:
            break
print(max(ans))