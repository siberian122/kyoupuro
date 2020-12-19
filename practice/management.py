n = int(input())
l = [0 for i in range(n)]
a = list(map(int, input().split()))
for ai in a:
    l[ai-1] += 1
for li in l:
    print(li)
