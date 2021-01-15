n = int(input())
ans = ""
while n > 0:
    if n % 26 == 0:
        ans += "z"
        n = n//26 - 1
    else:
        ans += chr((n % 26) + 96)
        n //= 26
print(ans[::-1])
