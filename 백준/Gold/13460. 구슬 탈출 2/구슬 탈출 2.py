import sys
from collections import deque

n, m = map(int, input().split())
graph = []
red = 0
blue = 0

for _ in range(n):
    graph.append(list(input().strip()))
    
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

# 완전 탐색 가능 (인덱스 에러 i, j로 수정 완료!)
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'B':
            blue = (i, j)
        elif graph[i][j] == 'R':
            red = (i, j)

q = deque([])
# 큐에 빨간 구슬, 파란 구슬, 그리고 '시간'을 한 덩어리로 묶어서 넣습니다.
q.append((red[0], red[1], blue[0], blue[1], 0))

# 두 구슬이 '동시에' 어디 있는지 기억해야 하므로 4차원 배열을 씁니다.
visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
visited[red[0]][red[1]][blue[0]][blue[1]] = True

# 구슬을 벽이나 구멍을 만날 때까지 끝까지 굴리는 함수
def move(x, y, dx, dy):
    count = 0
    while graph[x + dx][y + dy] != '#' and graph[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

while q:
    rx, ry, bx, by, time = q.popleft()
    
    # 10번 넘게 움직였으면 이 경로는 실패
    if time >= 10:
        continue
        
    for dx, dy in zip(dxs, dys):
        # 각각 굴려봅니다.
        nrx, nry, r_count = move(rx, ry, dx, dy)
        nbx, nby, b_count = move(bx, by, dx, dy)
        
        # 파란 구슬이 구멍에 빠지면 실패한 경로이므로 무시 (continue)
        if graph[nbx][nby] == 'O':
            continue
            
        # 빨간 구슬만 구멍에 빠졌다면 성공! 시간 출력하고 프로그램 종료
        if graph[nrx][nry] == 'O':
            print(time + 1)
            exit()
            
        # 두 구슬이 같은 위치에 멈췄을 때 겹치지 않게 뒤로 빼주기
        if nrx == nbx and nry == nby:
            if r_count > b_count:
                nrx -= dx
                nry -= dy
            else:
                nbx -= dx
                nby -= dy
                
        # 아직 방문하지 않은 상태라면 큐에 넣기
        if not visited[nrx][nry][nbx][nby]:
            visited[nrx][nry][nbx][nby] = True
            q.append((nrx, nry, nbx, nby, time + 1))

# 큐가 다 빌 때까지 exit()를 못 만났다면 탈출 불가능하므로 -1
print(-1)