s = input()
cnt = True
for _ in range(int(input())):
    q = list(input().split())

    if q[0] == "1":
        cnt = not bool(cnt)
    else:
        if q[1] == "1":
            if cnt:
                s = q[-1]+s
            else:
                s += q[-1]
        else:
            if cnt:
                s += q[-1]
            else:
                s = q[-1]+s
if cnt:
    print(s)
else:
    print(s[::-1])
