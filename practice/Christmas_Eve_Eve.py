n=int(input())
p=[int(input()) for _ in range(n)]
p.sort()
p[-1]=p[-1]//2
print(sum(p))