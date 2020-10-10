import random
l=[]
for i in range(20000):
    l.append(random.randint(0,200000))
print(*l)