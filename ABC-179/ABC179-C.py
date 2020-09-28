
n=int(input())
ans=0
for num in range(1,n):
    ans+=(n-1)//num
print(int(ans))