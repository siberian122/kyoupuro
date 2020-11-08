n=int(input())
a=list(map(int,input().split()))
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors
dic={}
for i in a:
    l=make_divisors(i)
    for j in l:
        if j not in dic:
            dic[j]=1
        else:
            dic[j]+=1
del dic[1]
print(max(dic,key=dic.get))