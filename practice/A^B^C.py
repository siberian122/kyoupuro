a, b, c = map(int, input().split())
n = b**c % 4
if n == 0:
    n = 4
print(a ** n % 10)
