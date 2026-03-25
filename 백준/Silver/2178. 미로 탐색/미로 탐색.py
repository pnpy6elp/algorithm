import sys
from collections import deque
input = sys.stdin.readline
# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 
n, m = map(int, input().split())
# 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
cnt_li = [[0] * m for _ in range(n)]

def in_range(x , y):
    return (0 <= x and x < n and 0 <= y and y <m)
def can_go(x, y):
    return in_range(x, y) and graph[x][y] and not visited[x][y]


def bfs():
    q = deque([(0,0)])
    visited[0][0] = True
    cnt_li[0][0] = 1 # 시작점의 거리는 1로 시작
    
    while q:
        x, y = q.popleft()
        dxs, dys = [0,1,0,-1], [1,0,-1,0]
        
        for dx, dy in zip(dxs, dys):
            point_x, point_y = x + dx, y + dy
            
            if can_go(point_x, point_y):
                # 1. 큐에 넣기 전에 무조건 방문 처리! (메모리 초과 방지)
                visited[point_x][point_y] = True
                
                # 2. 내 거리는 '직전 칸의 거리 + 1' (최단 거리 계산)
                cnt_li[point_x][point_y] = cnt_li[x][y] + 1
                
                q.append((point_x, point_y))
bfs()
chk = 1 if visited[n - 1][m - 1] else 0
if chk:
    print(cnt_li[n - 1][m - 1])
else:
    print()