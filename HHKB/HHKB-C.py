def main():
    n=int(input())
    p=list(map(int,input().split()))
    l=[0 for _ in range(max(p)+2)]
    cnt=0
    for i in p:
        l[i]=1
        if l[cnt]==0:
            print(cnt)
        else:
            while True:
                cnt+=1
                if l[cnt]==0:
                    break
            print(cnt)

main()
