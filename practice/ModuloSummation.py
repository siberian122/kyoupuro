n = int(input())
a = list(map(int, input().split()))
l = [x-1 for x in a]
print(sum(l))
