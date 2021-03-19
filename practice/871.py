n = int(input())
ans = "No"
for i in range(10):
    for j in range(10):
        if i * j == n:
            ans = "Yes"
            break
print(ans)
