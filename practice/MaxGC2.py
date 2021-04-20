import math
a, b = map(int, input().split())
for i in reversed(range(1, b+1)):
    if a//i + bool(a % i) < b//i:
        exit(print(i))
