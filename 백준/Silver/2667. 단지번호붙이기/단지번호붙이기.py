import sys
input = sys.stdin.readline

n = int(input().strip())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and graph[x][y] == 1

# 단지 크기를 저장할 변수 (글로벌로 사용)
cnt = 0 

def dfs(x, y):
    global cnt
    # 1. 들어오자마자 방문 처리! (무한 루프 방지)
    visited[x][y] = True
    cnt += 1
    
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        # 2. 다음 칸으로 갈 수 있으면 재귀 호출
        if can_go(new_x, new_y):
            dfs(new_x, new_y)

res = 0
res_li = []

for i in range(n):
    for j in range(n):
        # 3. 새로운 단지의 시작점을 발견하면!
        if can_go(i, j):
            cnt = 0       # 카운트 초기화
            dfs(i, j)     # DFS 탐색 시작 (탐색하면서 cnt가 쑥쑥 오름)
            res += 1      # 단지 개수 +1
            res_li.append(cnt) # 완성된 단지 크기 저장

print(res)
res_li.sort()
for rr in res_li:
    print(rr)