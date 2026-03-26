import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# zip() 대신 튜플을 직접 순회하는 것이 미세하게 더 빠릅니다.
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

def solve():
    year = 0
    while True:
        visited = [[False] * m for _ in range(n)]
        chunks = 0
        melt_list = [] # 이번 턴에 녹아야 할 빙산의 좌표와 녹을 양을 기록
        
        for i in range(n):
            for j in range(m):
                # 얼음이 있고 방문하지 않은 곳을 만나면 BFS 시작
                if graph[i][j] > 0 and not visited[i][j]:
                    chunks += 1
                    
                    # 💡 최적화 1: 탐색 중 덩어리가 2개 이상 발견되면 즉시 종료
                    if chunks >= 2:
                        print(year)
                        return
                        
                    # BFS 탐색 시작
                    queue = deque([(i, j)])
                    visited[i][j] = True
                    
                    while queue:
                        x, y = queue.popleft()
                        sea_count = 0 # 인접한 바다(0)의 개수
                        
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            
                            if 0 <= nx < n and 0 <= ny < m:
                                # 주변이 바다라면 sea_count 증가
                                if graph[nx][ny] == 0:
                                    sea_count += 1
                                # 주변이 얼음이고 방문 안 했다면 큐에 추가
                                elif graph[nx][ny] > 0 and not visited[nx][ny]:
                                    visited[nx][ny] = True
                                    queue.append((nx, ny))
                                    
                        # 최적화 2: 덩어리 탐색과 동시에 '녹을 양'을 계산해서 저장
                        if sea_count > 0:
                            melt_list.append((x, y, sea_count))
        
        # 빙산이 다 녹았는데도 위에서 return 되지 않았다면 덩어리가 0개라는 뜻
        if chunks == 0:
            print(0)
            return
            
        # 기록해둔 정보를 바탕으로 한꺼번에 빙산을 녹임
        for x, y, sea in melt_list:
            graph[x][y] -= sea
            if graph[x][y] < 0:
                graph[x][y] = 0
                
        year += 1

solve()