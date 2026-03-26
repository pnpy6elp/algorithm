from collections import deque

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

# 아기 상어 초기 위치 찾기
for i in range(n):
    for j in range(n):
        if mat[i][j] == 9:
            baby_x, baby_y = i, j
            mat[i][j] = 0

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs(bx, by, size):
    q = deque([(bx, by)])
    dist = [[-1] * n for _ in range(n)]
    dist[bx][by] = 0
    
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            # 갈 수 있는 곳(빈칸이거나 크기가 작거나 같은 물고기)
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1 and size >= mat[nx][ny]:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    return dist

size = 2
time = 0
current_feed = 0

while True:
    dist = bfs(baby_x, baby_y, size)
    fish = []
    
    # 먹을 수 있는 물고기 탐색
    for i in range(n):
        for j in range(n):
            if 0 < mat[i][j] < size and dist[i][j] != -1:
                # (거리, x좌표, y좌표) 순서로 튜플 저장!!!
                fish.append((dist[i][j], i, j))
                
    # 더 이상 먹을 물고기가 없으면 종료
    if not fish:
        print(time)
        break
        
    # 거리 -> x(위) -> y(왼쪽) 순으로 자동 오름차순 정렬됨
    fish.sort()
    
    # 정렬된 리스트의 첫 번째(0번 인덱스)가 무조건 타겟!
    min_dist, target_x, target_y = fish[0]
    
    # 상어 이동 및 먹기 처리
    baby_x, baby_y = target_x, target_y
    mat[baby_x][baby_y] = 0
    time += min_dist
    current_feed += 1
    
    if current_feed == size:
        size += 1
        current_feed = 0