n=input()
if n[0]=='1':
    ans=(len(n)-1)*9
else:
    ans=(len(n)-1)*9+int(n[0])
print(ans)