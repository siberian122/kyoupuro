n = int(input())
a = list(map(int, input().split()))
cnt = 0
even = 0
for i in a:
    if i % 2 == 0 and i % 3 != 0 and i % 5 != 0:
        exit(print("DENIED"))

print("APPROVED")
