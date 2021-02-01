n = int(input())
x = list(map(int, input().split()))
xx = sorted(x)
num = n//2
low_ans = xx[num-1]
up_ans = xx[num]
for i in x:
    if i > low_ans:
        print(low_ans)
    else:
        print(up_ans)
