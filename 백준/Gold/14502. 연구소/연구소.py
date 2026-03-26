n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

blank = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            blank.append((i,j))
            
def comb(arr, n):
    res = []
    if n == 0:
        return [[]]
    for i in range(0, len(arr)):
        first = arr[i]
        rest = arr[i+1:]
        for k in comb(rest, n-1):
            res.append([first]+k)
    return res

# 2 바이러스, 1 벽, 0 빈칸
from collections import deque
dxs, dys = [0,1,0,-1], [1,0,-1,0]
walls = comb(blank, 3)
cnt_li = []
for wall in walls:
    new_graph = [arr[:] for arr in graph]
    for w in wall:
        new_graph[w[0]][w[1]] = 1
    q = deque([])
    # 바이러스 출발점 여러개니까 큐에 다 넣기
    for i in range(n):
        for j in range(m):
            if new_graph[i][j]==2:
                q.append((i,j))
                
    while q:
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if (0<=nx<n) and (0<=ny<m) and new_graph[nx][ny]==0:
                new_graph[nx][ny] = 2
                q.append((nx,ny))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if new_graph[i][j] == 0:
                cnt += 1
    cnt_li.append(cnt)
print(max(cnt_li))
        
    
    
        