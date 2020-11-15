sx,sy,gx,gy=map(int,input().split())
gy=-gy
num=(gx-sx)/(gy-sy)*(-sy)+sx
print(num)