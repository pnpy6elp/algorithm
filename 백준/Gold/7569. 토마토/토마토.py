import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())

# 3차원 배열 입력 받기 (층 단위로 쌓임)
arr = []
for _ in range(h):
    arr1 = [list(map(int, input().split())) for _ in range(n)]
    arr.append(arr1)

q = deque()

# 동시다발적인 bfs -> queue에 시작점들 다 집어넣기

for z in range(h):       # 높이 (층)
    for x in range(n):   # 세로 (행)
        for y in range(m): # 가로 (열)
            if arr[z][x][y] == 1:
                q.append((z, x, y))

# BFS 탐색 시작 (함수로 안 빼고 바로 돌려도 됩니다)
dzs = [1, -1, 0, 0, 0, 0] # 층(높이)
dxs = [0, 0, 1, -1, 0, 0] # 행(x)
dys = [0, 0, 0, 0, 1, -1] # 열(y)

while q:
    # 💡 핵심 2: 큐에서 꺼낸 좌표로 탐색해야 합니다!
    z, x, y = q.popleft()
    
    for dz, dx, dy in zip(dzs, dxs, dys):
        nz, nx, ny = z + dz, x + dx, y + dy
        
        # 범위 체크: 층(0~h-1), 행(0~n-1), 열(0~m-1)
        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
            # 아직 안 익은 토마토(0)라면?
            if arr[nz][nx][ny] == 0:
                # 💡 핵심 3: 내 일수 = 직전 토마토 일수 + 1 (visited 대신 사용)
                arr[nz][nx][ny] = arr[z][x][y] + 1
                q.append((nz, nx, ny))

# ----------------- 탐색 종료 후 결과 확인 -----------------
max_days = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if arr[z][x][y] == 0:
                # 안 익은 토마토가 하나라도 남아있으면 실패
                print(-1)
                exit()
            # 가장 오래 걸린 일수 찾기
            max_days = max(max_days, arr[z][x][y])

# 처음 시작이 1이었으므로, 총 걸린 일수는 -1을 해줘야 함
print(max_days - 1)