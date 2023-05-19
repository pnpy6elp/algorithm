from collections import deque
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
 
def BFS():
    q.append((i, j))
    t = 1
    check[i][j] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and MAP[nx][ny] == 1 and check[nx][ny] == 0:
                check[nx][ny] = 1
                q.append((nx, ny))
                t += 1
    return t
 
N, M, K = map(int, input().split()) # N: 세로, M: 가로 K: 음식물 갯수
MAP = [[0] * M for _ in range(N)]
check = [[0] * M for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    MAP[x-1][y-1] = 1
 
q = deque()
 
ans = 0
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 1 and check[i][j] == 0:
            res = BFS()
            if res > ans: ans = res
 
print(ans)