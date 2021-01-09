l = [list(map(int, input().split())) for _ in range(3)]
c_11 = l[0][0]
for i in range(3):
    for j in range(3):
        l[i][j] -= c_11

a_1 = 0
a_2 = l[1][0]
a_3 = l[2][0]
b_1 = 0
b_2 = l[0][1]
b_3 = l[0][2]

ans = "Yes"
if not a_2+b_2 == l[1][1]:
    ans = "No"
if not a_2+b_3 == l[1][2]:
    ans = "No"
if not a_3+b_2 == l[2][1]:
    ans = "No"
if not a_3+b_3 == l[2][2]:
    ans = "No"
print(ans)
