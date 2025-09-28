import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1] 

def solve():
    queue = deque()
    has_unripe = False 

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                queue.append((i, j))
            elif graph[i][j] == 0:
                has_unripe = True

    if not has_unripe:
        print(0)
        return


    while queue:
        x, y = queue.popleft()
        current_day = graph[x][y] 

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]


            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:

                graph[nx][ny] = current_day + 1
                queue.append((nx, ny))

    max_day = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                print(-1)
                return

            # 익은 토마토 중 최대 날짜를 찾습니다.
            max_day = max(max_day, graph[i][j])

    print(max_day - 1)

solve()