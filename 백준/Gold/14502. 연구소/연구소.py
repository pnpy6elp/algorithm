n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 0: 빈칸, 1: 벽, 2: 바이러스
# 완전 탐색 해도 괜찮려나?
# 1을 추가로 3개 더 채웠을 때 0의 최대 크기
from collections import deque
def in_range(x, y):
    return (0<=x<n) and (0<=y<m)

dxs, dys = [0,1,0,-1], [1,0,-1,0]


def comb(arr, n):
    res = []
    if n==0:
        return [[]]
    
    for i in range(0, len(arr)):
        elem = arr[i]
        rest = arr[i+1:]
        for c in comb(rest, n-1):
            res.append([elem]+c)
    return res

blank = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            blank.append((i,j))

wall_comb = comb(blank,3)

visited = [[False]*m for _ in range(n)]

def bfs(q,graph):
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx,ny) and graph[nx][ny]==0:
                graph[nx][ny] = 2
                q.append((nx,ny))
    return graph

cnt_li = []
for C in wall_comb:
    new_graph = [arr[:] for arr in graph]
    for w in C:
        new_graph[w[0]][w[1]] = 1
    q = deque([])
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                q.append((i,j))
    new_graph = bfs(q, new_graph)
    
    visited = [[False]*m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if new_graph[i][j]==0:
                cnt += 1
    cnt_li.append(cnt)
                
print(max(cnt_li))

