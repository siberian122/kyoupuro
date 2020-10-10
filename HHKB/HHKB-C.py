def main():
    n=int(input())
    p=list(map(int,input().split()))
    l=[0 for _ in range(max(p)+2)]
    #print(l)
    reserc=l.index
    for i in p:
        l[i]=1
        print(reserc(0))

main()
