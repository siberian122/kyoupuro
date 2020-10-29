x=int(input())
ans=1
if x<100:
    ans=0
else:
    syou=x//100
    amari=x%100
    if amari>syou*5:
        ans=0
print(ans)