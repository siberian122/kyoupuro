def isAvailable(y,x):
    if not (0 <= y < R):
		return False

	if not (0 <= x < C):
		return False
	if dist[y][x] != -1:
		return False
	if graph[y][x] != ".":
		return False
	return True

from collections import deque
import sys

R,C = map(int, input().split())
sy,sx = map(int, input().split())
sy -= 1; sx -= 1;
gy,gx = map(int, input().split())
gy -= 1; gx -= 1;
graph = [input() for _ in range(R)]
dist = [[-1]*C for _ in range(R)]
dist[sy][sx] = 0
d = deque()
d.append([sy,sx])

#for i in graph: print(i)
#for i in dist: print(*i)

#今いる場所の隣が通行可能か調べ、距離を代入してゴールになったら終了

while d:
	v = d.popleft()
	cy = v[0]; cx = v[1]; 
	next = [[cy, cx+1],[cy,cx-1],[cy+1,cx],[cy-1,cx]]
	for nex in next:
		ny = nex[0]; nx = nex[1]
		if isAvailable(ny, nx):
			dist[ny][nx] = dist[cy][cx] + 1
			if [ny,nx] == [gy,gx]:
				print(dist[ny][nx])
				sys.exit()
			else:
				d.append([ny,nx])
				# for i in dist: print(*i)
