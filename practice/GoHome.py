x = int(input())
ans = 0
for i in range(1, x+1):
    if i*(i+1)/2 >= x:
        ans = i
        break
print(ans)
