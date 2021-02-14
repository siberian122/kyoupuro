t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    num = r-l*2
    if num < 0:
        print(0)
    print((num+1)*(num+2)//2)
