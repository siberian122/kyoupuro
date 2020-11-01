n=int(input())
num=0
for _ in range(n):
    a,b=map(int,input().split())
    num+=(b+a)*((b-a+1)//2)
    if (b-a+1) %2!=0:
        num+=(a+(b-a+1)//2)
        
    #print(num)
print(num)  