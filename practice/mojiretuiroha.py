n,l=map(int,input().split())
L=[]
for i in range(n):
    L.append(input())
L.sort()
print(''.join(L))