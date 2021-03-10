n = int(input())
a = list(map(int, input().split()))
A = set(a)
if len(a) == len(A):
    print("Yes")
else:
    print("No")
