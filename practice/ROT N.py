n = int(input())
s = input()
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(len(alph))
ans = ""
for i in s:
    num = alph.index(i)
    if num + n >= 25:
        num = num - 26
    ans += alph[num+n]
print(ans)
