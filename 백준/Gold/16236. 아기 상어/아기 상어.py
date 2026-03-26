n = int(input())
# 정사각형
mat = [list(map(int, input().split())) for _ in range(n)]
# 아기상어 위치

for i in range(n):
    for j in range(n):
        if mat[i][j] == 9:
            baby_x, baby_y = i, j
            mat[i][j] = 0
            
from collections import deque


dxs, dys = [0,1,0,-1], [1,0,-1,0]

def bfs(q,visited,size):
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==-1 and size >= mat[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
    return visited

size = 2
time = 0
current_feed = 0

while True:
    q = deque([(baby_x, baby_y)]) # 현 위치에서 출발
    dist = [[-1]*n for _ in range(n)]
    dist[baby_x][baby_y] = 0
    dist = bfs(q,dist,size)
    fish = []
    for i in range(n):
        for j in range(n):
            if 0 < mat[i][j] < size and dist[i][j] != -1:
                fish.append([(i,j),dist[i][j]])
    if len(fish) == 0:
        print(time)
        exit()
    elif len(fish) == 1:
        baby_x, baby_y = fish[0][0]
        mat[baby_x][baby_y] = 0
        time += fish[0][1]
        current_feed += 1
        if current_feed == size:
            size += 1
            current_feed = 0
    else:
        fish.sort(key=lambda x:x[1])
        min_dist = fish[0][1]
        new_fish = [f for f in fish if f[1]==min_dist]
        if len(new_fish)==1:
            baby_x, baby_y = new_fish[0][0]
            mat[baby_x][baby_y] = 0
            time += new_fish[0][1]
            current_feed += 1
            if current_feed == size:
                size += 1
                current_feed = 0
        else:
            new_fish.sort(key=lambda x:x[0][0])
            min_x = new_fish[0][0][0]
            new_fish = [f for f in new_fish if f[0][0]==min_x]
            if len(new_fish)==1:
                baby_x, baby_y = new_fish[0][0]
                mat[baby_x][baby_y] = 0
                time += new_fish[0][1]
                current_feed += 1
                if current_feed == size:
                    size += 1
                    current_feed = 0
            else:
                new_fish.sort(key=lambda x:x[0][1])
                baby_x, baby_y = new_fish[0][0]
                mat[baby_x][baby_y] = 0
                time += new_fish[0][1]
                current_feed += 1
                if current_feed == size:
                    size += 1
                    current_feed = 0
