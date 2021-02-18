n, a, b, c, d = map(int, input().split())
s = input()
rock = False
non = []
cnt = 0

for i in range(max(c, d)):
    if s[i] == "#":
        if rock:
            exit(print("No"))
        else:
            rock = True
        non.append(cnt)
        cnt = 0
    else:
        rock = False
        cnt += 1
non.append(cnt)
# print(non)
if c < d:
    print("Yes")
else:
    if max(non) > 2:
        print("Yes")
    else:
        print("No")
