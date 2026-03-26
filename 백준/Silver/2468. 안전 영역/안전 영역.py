import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input().strip())
graph = [list(map(int, input().split())) for _ in range(n)]

# 최대 높이 구하기
max_h = max(map(max, graph))

# 비가 오지 않을 때(h=0) 맵 전체가 1개의 영역이 됨
ans = 1 

# 방향 벡터 (튜플 사용이 미세하게 더 빠름)
directions = ((0,1), (1,0), (0,-1), (-1,0))

# 1부터 최대 높이-1 까지만 검사하면 됨 (최대 높이만큼 비가 오면 무조건 영역은 0개)
for h in range(1, max_h):
    visited = [[False] * n for _ in range(n)]
    res = 0
    
    def dfs(x, y):
        visited[x][y] = True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 함수 호출 대신 조건문 직접 작성 (속도 향상)
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] > h:
                    dfs(nx, ny)

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > h:
                res += 1
                dfs(i, j)
                
    ans = max(ans, res)

print(ans)