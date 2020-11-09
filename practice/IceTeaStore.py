q,h,s,d=map(int,input().split())
n=int(input())
l=min(q*4,h*2,s)
dl=min(l*2,d)
ans=(n//2)*dl+(n%2)*l
print(ans)