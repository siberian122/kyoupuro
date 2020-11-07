n=[int(x) for x in input()]
ans=max(sum(n),(len(n)-1)*9+(n[0]-1))
print(ans)