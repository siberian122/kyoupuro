n = int(input())
a = list(map(int, input().split()))
cnt = 0
even = 0
for i in a:
    if i % 2 == 0:
        even += 1
        if i % 5 == 0 or i % 3 == 0:
            cnt += 1
            break
if cnt == even:
    print("APPROVED")
else:
    print("DENIED")
