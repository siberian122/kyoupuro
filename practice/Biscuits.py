n, p = map(int, input().split())
a = list(map(int, input().split()))
even, odd = 0, 0
for i in a:
    if i % 2:
        odd += 1
    else:
        even += 1
if odd == 0:
    if p == 1:
        print(0)
    else:
        print(2**n)
else:
    print(2**(n-1))
