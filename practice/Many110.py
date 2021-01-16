n = int(input())
t = input()
ans = 0
if t == "1":
    ans = 2*(10**10)
elif t == "11":
    ans = 10**10
else:
    num = t.count("0")
    if t[-1] == "0":
        ans = 10**10-num+1
    else:
        ans = 10**10-num
if t not in "110" * (n//+1):
    ans = 0
print(ans)
