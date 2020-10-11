t=int(input())
for _ in range(t):
    n=int(input())
    case=list(map(int,input().split()))
    winner=len(case)%2
    case.sort()
    winner=(case[0])%2
    if winner:
        print('Second')
    else:
        print('First')
