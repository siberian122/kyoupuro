n = int(input())
t = input()
ans=0
s="110"*10**6

if s[0:n] == t:
    ans=10**10-(n-1)//3
elif s[1:n+1] == t:
    ans=10**10 -n//3
elif s[2:n+2] == t:
    ans=10**10 -(n+1)//3
print(ans)