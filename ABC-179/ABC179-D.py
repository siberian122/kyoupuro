N=int(input())
i=2
ans=dict()
n=N
while i*i <=N:
	while n%i==0:
		n=n//i
		if i in ans:
			ans[i]+=1
		else:
			ans[i]=1
	i+=1
if n!=1:
	ans[n]=1
print(list(ans.items()))