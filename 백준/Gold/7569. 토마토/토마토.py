import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

arr = []
for _ in range(h):
    arr1 = [list(map(int, input().split())) for _ in range(n)]
    arr.append(arr1)

# arr[z][x][y] 순서에 유의하기! 층, 행, 렬

def in_range(z,x,y):
    return (z>=0 and z<h and x>=0 and x<n and y>=0 and y<m)
def can_go(z,x,y):
    return (in_range(z,x,y) and arr[z][x][y]==0)
q = deque([])
for z in range(h):
    for x in range(n):
        for y in range(m):
            if arr[z][x][y] == 1:
                q.append((z,x,y))
                
dzs = [1, -1, 0, 0, 0, 0] # 층(h)
dxs = [0, 0, 1, -1, 0, 0] # 행(x)
dys = [0, 0, 0, 0, 1, -1] # 열(y)

while q:
    z, x, y = q.popleft()
    
    for dz, dx, dy in zip(dzs, dxs, dys):
        nz, nx, ny = z + dz, x + dx, y + dy
        if can_go(nz, nx, ny):
            arr[nz][nx][ny] = arr[z][x][y] + 1
            q.append((nz, nx, ny))
            
max_days = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if arr[z][x][y] == 0:
                print(-1)
                exit()
            max_days = max(max_days, arr[z][x][y])
            
print(max_days-1)