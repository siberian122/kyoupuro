n = int(input())
s = input()
t = input()
num = 0
for i in range(n):
    if s[i:] == t[:n-i]:
        num = n-i
        break
print(2*n-num)
