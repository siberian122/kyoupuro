abcd = input()
# bit全探索
for i in range(2**3):
    a = int(abcd[0])
    ans = abcd[0]
    for j in range(3):
        if (i >> j) & 1:
            a += int(abcd[j+1])
            ans += "+"+abcd[j+1]
        else:
            a -= int(abcd[j+1])
            ans += "-"+abcd[j+1]
    if a == 7:
        ans += "=7"
        print(ans)
        break
