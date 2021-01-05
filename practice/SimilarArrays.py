n = int(input())
a = list(map(int, input().split()))
even = 0
for i in a:
    if not i % 2:
        even += 1
print(3**n-2**even)
