n = int(input())
a = list(map(int, input().split()))
b = max(a[:2**n//2])
c = max(a[2**n//2:])
#print(b, c)
print(a.index(min(b, c))+1)
