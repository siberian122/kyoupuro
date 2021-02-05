s = input()
cnt = []
for i in range(3):
    cnt.append(s.count(chr(ord("a")+i)))
c = cnt[-1]
flag = 1
for i in cnt:
    if abs(c-i) > 1:
        flag = 0
        break
    c = i
if flag:
    print("YES")
else:
    print("NO")
