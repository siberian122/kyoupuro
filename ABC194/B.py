n = int(input())
person = []
for i in range(n):
    a, b = map(int, input().split())
    person.append([a, b, i])
wa = min([x+y for x, y, z in person])

cnt_a = sorted(person, key=lambda x: x[0])
cnt_b = sorted(person, key=lambda x: x[1])
a = cnt_a[1][0]
b = cnt_b[1][1]

"""
print(cnt_a)
print(cnt_b)
print(cnt_a[0][2])
"""
if cnt_a[0][2] == cnt_b[0][2]:  # 同じ人が速い
    if cnt_a[0][0] > cnt_b[0][1]:  # Aのほうが遅い
        cnt = a
    elif cnt_a[0][0] < cnt_b[0][1]:
        cnt = b
    else:  # 一緒だったら次のAとBの小さいほう
        cnt = min(a, b)
    print(min(wa, cnt))

else:
    print(max(cnt_a[0][0], cnt_b[0][1]))
