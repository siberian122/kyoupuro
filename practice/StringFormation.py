s = input()
cnt = 0
front = ""
end = ""
for _ in range(int(input())):
    q = list(input().split())

    if q[0] == "1":
        cnt = cnt ^ 1
    else:
        if int(q[1])-1 == cnt:
            front = q[2]+front
        else:
            end = end+q[2]
s = front + s + end
if cnt:
    print(s[::-1])
else:
    print(s)
