n=int(input())
ans=[-1]
for i in range(1,40):
    for l in range(1,40):
        if 3**i+5**l==n:
            ans=[i,l]
            break
print(*ans)
