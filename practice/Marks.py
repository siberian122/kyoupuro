n, k = map(int, input().split())
a = list(map(int, input().split()))
past = []
for i in range(k-1, n):
    num = 1
    for l in range(k):
        num *= a[i-l]
    past.append(num)
for i in range(len(past)-1):
    if past[i] < past[i+1]:
        print("Yes")
    else:
        print("No")
