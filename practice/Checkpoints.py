n,m=map(int,input().split())
student=[]
point=[]
for _ in range(n):
    s=list(map(int,input().split()))
    student.append(s)
for _ in range(m):
    s=list(map(int,input().split()))
    point.append(s)
for i in student:
    a,b=i[0],i[1]
    points=int
    man=10**9
    for j in range(m-1,-1,-1):
        c,d=point[j][0],point[j][1]
        num=abs(a-c)+abs(b-d)
        if man>=num:
            man=num
            points=j+1
    print(points)
    