import re
n=int(input())
s=input()
t=''
while not s=='':
    t+=(s[0])
    s=s[1:]
    if t[-3:]=='fox':
        t=t[:-3]
    s=t+s
print(len(t))
