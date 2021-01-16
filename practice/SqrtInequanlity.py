a, b, c = map(int, input().split())
d = c-a-b
num = 4*a*b
if d < 0:
    ans = "No"
else:
    if d*d > num:
        ans = "Yes"
    else:
        ans = "No"
print(ans)
