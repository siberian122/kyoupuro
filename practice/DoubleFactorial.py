n=int(input())
if n%2:
    print(0)
else:
    ans=0
    i=5
    while True:
        if i*2>n:
            break
        ans+=n//(i*2)
        i*=5
    print(ans)