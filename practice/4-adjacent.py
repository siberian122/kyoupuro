n = int(input())
a = list(map(int, input().split()))
four = 0
two = 0
for i in a:
    if i % 4 == 0:
        four += 1
    elif i % 2 == 0:
        two += 1
if n//2 <= (four + two//2):
    print("Yes")
else:
    print("No")
